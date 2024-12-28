# Documentation Scraper

A configurable web scraper that converts API documentation websites to Markdown format. This tool can be used for any API documentation site with similar structure.

The output document is useful when Programming with AI as the output serve as RAG for less hallucination.

## Features

- Concurrent scraping with configurable number of workers
- Rate limiting to prevent server overload
- URL exclusion patterns
- Depth-limited crawling
- Converts HTML to clean Markdown
- Maintains directory structure
- Handles relative links and images
- Configurable retry mechanism

## Setup

1. Clone the repository:
```bash
git clone https://github.com/dabaspark/documentation_scraper.git
cd documentation_scraper
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the scraper by editing `config.json`:
```json
{
    "base_url": "https://api-docs.deepseek.com",  // Target API documentation URL
    "output_dir": "output",                        // Output directory name
    "exclude_paths": ["zh-cn"],                    // Paths to exclude
    "max_depth": 5,                               // Maximum crawl depth
    "max_workers": 4,                             // Number of concurrent workers
    "rate_limit_delay": {
        "min": 1,
        "max": 3
    },
    "retry_config": {
        "total": 5,                               // Number of retry attempts
        "backoff_factor": 0.5,                    // Retry backoff factor
        "status_forcelist": [500, 502, 503, 504, 404]  // Status codes to retry
    },
    "request_timeout": 10                         // Request timeout in seconds
    "combine_output": true,                       // combine all docs into one file  
    "combined_file_name": "combined_docs.md"      // name of the combined file output
}
```

4. Run the scraper:
```bash
python scraper.py
```

## Configuration Options

### Basic Settings:
- `base_url`: The root URL of the API documentation to scrape
  ```json
  "base_url": "https://api-docs.deepseek.com"  // Scrape this site
  "base_url": "https://docs.your-api.com"      // Or your own site
  ```

- `output_dir`: Directory where markdown files will be saved
  ```json
  "output_dir": "output"     // Default output folder
  "output_dir": "docs/api"   // Custom nested directory
  ```

- `exclude_paths`: List of path segments to exclude from scraping. For example, if you set `"exclude_paths": ["zh-cn"]`, the following URLs will be excluded:
    - `https://api-docs.deepseek.com/zh-cn/guides`
    - `https://api-docs.deepseek.com/zh-cn/news/news1120`
    ```json
    "exclude_paths": ["zh-cn"]                    // Skip Chinese docs
    "exclude_paths": ["zh-cn", "fr", "beta"]      // Skip multiple paths
    "exclude_paths": ["v1", "deprecated"]         // Skip old versions
    ```

- `max_depth`: Maximum depth level for crawling
  ```json
  "max_depth": 1    // Only root pages (/, /page1, /page2)
  "max_depth": 2    // Include one level of subdirectories (/docs/page1)
  "max_depth": 5    // Deep crawl (recommended for most sites)
  ```

- `max_workers`: Number of concurrent threads for processing
  ```json
  "max_workers": 1    // Sequential processing, safest but slowest
  "max_workers": 4    // Balanced approach (recommended)
  "max_workers": 8    // Faster but may overwhelm some servers
  ```

- `combine_output`: Option to combine all markdown files into a single file. When enabled, the combined output will maintain the structure using markdown headers and include all content in one file. This is useful for creating a single reference document for AI/LLM purposes.

    Note: Individual files are still saved separately in addition to the combined file when this option is enabled.
    ```json
    "combine_output": true,    // Enable combined output file
    "combine_output": false    // Keep files separate only
    ```

- `combined_file_name`: Name of the combined output file
  ```json
  "combined_file_name": "combined_docs.md"      // Default name
  "combined_file_name": "full_documentation.md"  // Custom name
  ```

### Rate Limiting:
- `rate_limit_delay`: Controls the delay between requests
  ```json
  "rate_limit_delay": {
    "min": 0.1,    // Very aggressive (only for testing)
    "max": 0.5     // May get your IP blocked
  }
  
  "rate_limit_delay": {
    "min": 1,      // Recommended minimum
    "max": 3       // Balanced approach
  }
  
  "rate_limit_delay": {
    "min": 3,      // Very polite
    "max": 5       // Good for production use
  }
  ```

### Advanced Settings:
- `retry_config`: Controls the retry behavior
  ```json
  "retry_config": {
    "total": 3,                               // Fewer retries, fail faster
    "backoff_factor": 0.5,                    // Wait 0.5s, 1s, 2s between retries
    "status_forcelist": [500, 502, 503, 504]  // Only retry server errors
  }
  
  "retry_config": {
    "total": 5,                               // More retries, more resilient
    "backoff_factor": 1,                      // Wait 1s, 2s, 4s, 8s, 16s
    "status_forcelist": [500, 502, 503, 504, 404, 429]  // Also retry rate limits
  }
  ```

- `request_timeout`: Timeout for HTTP requests in seconds
  ```json
  "request_timeout": 5     // Fail fast on slow responses
  "request_timeout": 10    // Default balanced timeout
  "request_timeout": 30    // Wait longer for slow servers
  ```

### Example Configurations

#### Fast Local Testing:
```json
{
    "max_workers": 8,
    "rate_limit_delay": {
        "min": 0.1,
        "max": 0.5
    },
    "request_timeout": 5
}
```

#### Production Scraping:
```json
{
    "max_workers": 4,
    "rate_limit_delay": {
        "min": 3,
        "max": 5
    },
    "retry_config": {
        "total": 5,
        "backoff_factor": 1,
        "status_forcelist": [500, 502, 503, 504, 404, 429]
    },
    "request_timeout": 30
}
```

#### Minimal Resource Usage:
```json
{
    "max_workers": 1,
    "rate_limit_delay": {
        "min": 5,
        "max": 10
    },
    "max_depth": 3
}
```

## Example Use Cases

### Scraping Deepseek API Docs:
```json
{
    "base_url": "https://api-docs.deepseek.com",
    "exclude_paths": ["zh-cn"]
}
```

### Scraping with Aggressive Rate Limiting:
```json
{
    "rate_limit_delay": {
        "min": 3,
        "max": 5
    },
    "max_workers": 2
}
```

## Output Structure

The documentation will be saved in two formats when `combine_output` is enabled:

1. Individual files (default structure):
```
output/
├── section1/
│   ├── page1.md
│   └── page2.md
├── section2/
│   └── page3.md
└── index.md
```

2. Combined file (when enabled):
```
output/
└── combined_docs.md  (or custom name)
```

The combined file will maintain the hierarchy using markdown headers and include all content in a single file, which can be useful for:
- Full-text search
- Easier importing into documentation systems
- Single-file reference
- AI/LLM training data

## Good Practice Guidelines

1. Always check the website's robots.txt
2. Use appropriate rate limiting
3. Don't overload servers with too many concurrent requests
4. Consider running during off-peak hours
5. Backup any existing output directory before running

## Contributing

Feel free to submit issues and enhancement requests!
