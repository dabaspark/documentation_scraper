import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, quote, unquote
import html2text
import json
from typing import Set, Dict, List
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# Load configuration
def load_config() -> Dict:
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"exclude_paths": [], "exclude_patterns": [], "max_depth": 5}

CONFIG = load_config()
BASE_URL = CONFIG.get('base_url', 'https://api-docs.deepseek.com')
OUTPUT_DIR = CONFIG.get('output_dir', 'output')
TIMEOUT = CONFIG.get('request_timeout', 10)
RETRY_CONFIG = CONFIG.get('retry_config', {
    'total': 5,
    'backoff_factor': 0.5,
    'status_forcelist': [500, 502, 503, 504, 404]
})
RATE_LIMIT = CONFIG.get('rate_limit_delay', {'min': 1, 'max': 3})

visited_urls: Set[str] = set()

# Add thread-safe lock for visited_urls
visited_urls_lock = Lock()

def is_excluded_path(url: str) -> bool:
    """Check if URL path contains any excluded paths"""
    parsed = urlparse(url)
    path = parsed.path.lstrip('/')
    return any(excluded in path.split('/') for excluded in CONFIG['exclude_paths'])

def is_valid_url(url: str) -> bool:
    """Check if URL belongs to our target domain and is not excluded"""
    parsed = urlparse(url)
    return (parsed.netloc == urlparse(BASE_URL).netloc and 
            not is_excluded_path(url))

def normalize_url(url: str) -> str:
    """Remove fragments and trailing slashes from URL"""
    parsed = urlparse(url)
    # Reconstruct URL without fragment
    normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path.rstrip('/')}"
    return normalized

def clean_url(url: str) -> str:
    """Clean and properly encode URLs, but remove fragments"""
    parsed = urlparse(url)
    # Encode the path portion of the URL
    path = quote(unquote(parsed.path), safe='/:')
    # Reconstruct the URL without fragment
    return f"{parsed.scheme}://{parsed.netloc}{path.rstrip('/')}"

def create_session():
    """Create a session with retry strategy"""
    session = requests.Session()
    retries = Retry(
        total=RETRY_CONFIG['total'],
        backoff_factor=RETRY_CONFIG['backoff_factor'],
        status_forcelist=RETRY_CONFIG['status_forcelist'],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def get_page_content(url):
    """Get page content with retry logic and random delay"""
    session = create_session()
    time.sleep(random.uniform(RATE_LIMIT['min'], RATE_LIMIT['max']))
    
    try:
        response = session.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {str(e)}")
        # Return empty string if failed after retries
        return ""

def get_all_page_links(url: str) -> set:
    """Extract all links from a page with retry logic"""
    session = create_session()
    links = set()
    
    try:
        # Random delay between 1 and 3 seconds
        time.sleep(random.uniform(1, 3))
        response = session.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(url, href)
            if is_valid_url(full_url):
                # Normalize URL to avoid duplicates with fragments
                normalized_url = normalize_url(full_url)
                links.add(normalized_url)
        
    except requests.exceptions.RequestException as e:
        print(f"Error getting links from {url}: {str(e)}")
    except Exception as e:
        print(f"Unexpected error processing {url}: {str(e)}")
    
    return links

def get_url_depth(url: str) -> int:
    """Calculate depth based on URL path segments"""
    parsed = urlparse(url)
    # Split path into segments and filter out empty strings
    path_segments = [seg for seg in parsed.path.split('/') if seg]
    return len(path_segments)

def process_url(url: str, max_depth: int) -> List[str]:
    """Process a single URL and return discovered links"""
    normalized_url = normalize_url(url)
    actual_depth = get_url_depth(url)
    
    if actual_depth >= max_depth:
        return []
        
    with visited_urls_lock:
        if normalized_url in visited_urls or is_excluded_path(normalized_url):
            return []
        visited_urls.add(normalized_url)
    
    print(f"Processing ({actual_depth}/{max_depth-1}): {normalized_url}")
    
    try:
        html_content = get_page_content(normalized_url)
        if not html_content:
            return []
            
        markdown_content = convert_to_markdown(html_content, normalized_url)
        
        relative_path = urlparse(normalized_url).path
        if not relative_path or relative_path == '/':
            relative_path = '/index'
        save_markdown(markdown_content, relative_path)
        
        return list(get_all_page_links(normalized_url))
                
    except Exception as e:
        print(f"Error processing {normalized_url}: {str(e)}")
        return []

def process_with_threadpool(start_url: str, max_depth: int, max_workers: int):
    """Process pages using a thread pool"""
    to_process = {start_url}
    processed = set()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while to_process:
            # Submit batch of URLs to process
            future_to_url = {
                executor.submit(process_url, url, max_depth): url 
                for url in to_process
            }
            
            # Clear to_process set for next batch
            to_process = set()
            
            # Process completed futures
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                processed.add(url)
                try:
                    # Add new discovered URLs to process
                    new_urls = future.result()
                    to_process.update(
                        url for url in new_urls 
                        if url not in processed 
                        and url not in visited_urls
                    )
                except Exception as e:
                    print(f"Error processing {url}: {str(e)}")

def setup_directories():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def convert_to_markdown(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Convert relative URLs to absolute
    for tag in soup.find_all(['a', 'img']):
        if tag.get('href'):
            tag['href'] = urljoin(base_url, tag['href'])
        if tag.get('src'):
            tag['src'] = urljoin(base_url, tag['src'])
    
    h = html2text.HTML2Text()
    h.inline_links = True
    h.body_width = 0
    return h.handle(str(soup))

def save_markdown(content, url_path):
    """Save markdown content with properly encoded filenames"""
    # Clean the URL path before using it as filename
    clean_path = unquote(url_path).strip('/')
    # Replace any remaining problematic characters
    clean_path = clean_path.replace('#', '-').replace('?', '-')
    
    file_path = os.path.join(OUTPUT_DIR, f"{clean_path}.md")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def combine_markdown_files():
    """Combine all markdown files in output directory into one file"""
    combined_content = []
    combined_file = CONFIG.get('combined_file_name', 'combined_docs.md')
    
    # Walk through the output directory
    for root, _, files in os.walk(OUTPUT_DIR):
        for file in sorted(files):
            if file.endswith('.md') and file != combined_file:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, OUTPUT_DIR)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add section header
                section_header = f"\n\n# {rel_path[:-3]}\n\n"  # Remove .md extension
                combined_content.append(section_header)
                combined_content.append(content)
    
    # Save combined content
    if combined_content:
        combined_file_path = os.path.join(OUTPUT_DIR, combined_file)
        with open(combined_file_path, 'w', encoding='utf-8') as f:
            f.write("".join(combined_content))
        print(f"Combined documentation saved to: {combined_file_path}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    max_workers = CONFIG.get('max_workers', 4)
    max_depth = CONFIG.get('max_depth', 5)
    
    # Start crawling from the base URL with thread pool
    process_with_threadpool(BASE_URL, max_depth, max_workers)
    
    # Combine markdown files if enabled
    if CONFIG.get('combine_output', False):
        combine_markdown_files()
    
    # Save a summary of processed URLs
    with open(os.path.join(OUTPUT_DIR, 'processed_urls.txt'), 'w', encoding='utf-8') as f:
        for url in sorted(visited_urls):
            f.write(f"{url}\n")

if __name__ == "__main__":
    main()
