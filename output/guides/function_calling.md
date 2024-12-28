[Skip to main content](https://api-docs.deepseek.com/guides/function_calling#__docusaurus_skipToContent_fallback)

[![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)**DeepSeek API Docs**](https://api-docs.deepseek.com/)

[ English](https://api-docs.deepseek.com/guides/function_calling)

  * [English](https://api-docs.deepseek.com/guides/function_calling)
  * [ä¸­æï¼ä¸­å½ï¼](https://api-docs.deepseek.com/zh-cn/guides/function_calling)



[DeepSeek Platform](https://platform.deepseek.com/)

  * [Quick Start](https://api-docs.deepseek.com/)

    * [Your First API Call](https://api-docs.deepseek.com/)
    * [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)
    * [The Temperature Parameter](https://api-docs.deepseek.com/quick_start/parameter_settings)
    * [Token & Token Usage](https://api-docs.deepseek.com/quick_start/token_usage)
    * [Rate Limit](https://api-docs.deepseek.com/quick_start/rate_limit)
    * [Error Codes](https://api-docs.deepseek.com/quick_start/error_codes)
  * [News](https://api-docs.deepseek.com/news/news1226)

    * [Introducing DeepSeek-V3 2024/12/26](https://api-docs.deepseek.com/news/news1226)
    * [DeepSeek-V2.5-1210 Release 2024/12/10](https://api-docs.deepseek.com/news/news1210)
    * [DeepSeek-R1-Lite Release 2024/11/20](https://api-docs.deepseek.com/news/news1120)
    * [DeepSeek-V2.5 Release 2024/09/05](https://api-docs.deepseek.com/news/news0905)
    * [Context Caching is Available 2024/08/02](https://api-docs.deepseek.com/news/news0802)
    * [New API Features 2024/07/25](https://api-docs.deepseek.com/news/news0725)
  * [API Reference](https://api-docs.deepseek.com/api/deepseek-api)

  * [API Guides](https://api-docs.deepseek.com/guides/multi_round_chat)

    * [Multi-round Conversation](https://api-docs.deepseek.com/guides/multi_round_chat)
    * [Chat Prefix Completion (Beta)](https://api-docs.deepseek.com/guides/chat_prefix_completion)
    * [FIM Completion (Beta)](https://api-docs.deepseek.com/guides/fim_completion)
    * [JSON Output](https://api-docs.deepseek.com/guides/json_mode)
    * [Function Calling](https://api-docs.deepseek.com/guides/function_calling)
    * [Context Caching](https://api-docs.deepseek.com/guides/kv_cache)
  * [Other Resources](https://github.com/deepseek-ai/awesome-deepseek-integration/tree/main)

    * [Integrations](https://github.com/deepseek-ai/awesome-deepseek-integration/tree/main)
    * [API Status Page](https://status.deepseek.com/)
  * [FAQ](https://api-docs.deepseek.com/faq)
  * [Change Log](https://api-docs.deepseek.com/updates)



  * [](https://api-docs.deepseek.com/)
  * API Guides
  * Function Calling



On this page

# Function Calling

Function Calling allows the model to call external tools to enhance its capabilities.

## Sample Code[â](https://api-docs.deepseek.com/guides/function_calling#sample-code "Direct link to Sample Code")

Here is an example of using Function Calling to get the current weather information of the user's location, demonstrated with complete Python code.

For the specific API format of Function Calling, please refer to the [Chat Completion](https://api-docs.deepseek.com/api/create-chat-completion/) documentation.
    
    
    from openai import OpenAI  
      
    def send_messages(messages):  
        response = client.chat.completions.create(  
            model="deepseek-chat",  
            messages=messages,  
            tools=tools  
        )  
        return response.choices[0].message  
      
    client = OpenAI(  
        api_key="<your api key>",  
        base_url="https://api.deepseek.com",  
    )  
      
    tools = [  
        {  
            "type": "function",  
            "function": {  
                "name": "get_weather",  
                "description": "Get weather of an location, the user shoud supply a location first",  
                "parameters": {  
                    "type": "object",  
                    "properties": {  
                        "location": {  
                            "type": "string",  
                            "description": "The city and state, e.g. San Francisco, CA",  
                        }  
                    },  
                    "required": ["location"]  
                },  
            }  
        },  
    ]  
      
    messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]  
    message = send_messages(messages)  
    print(f"User>\t {messages[0]['content']}")  
      
    tool = message.tool_calls[0]  
    messages.append(message)  
      
    messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24â"})  
    message = send_messages(messages)  
    print(f"Model>\t {message.content}")  
    

The execution flow of this example is as follows:

  1. User: Asks about the current weather in Hangzhou
  2. Model: Returns the function `get_weather({location: 'Hangzhou'})`
  3. User: Calls the function `get_weather({location: 'Hangzhou'})` and provides the result to the model
  4. Model: Returns in natural language, "The current temperature in Hangzhou is 24Â°C."



Note: In the above code, the functionality of the `get_weather` function needs to be provided by the user. The model itself does not execute specific functions.

[PreviousJSON Output](https://api-docs.deepseek.com/guides/json_mode)[NextContext Caching](https://api-docs.deepseek.com/guides/kv_cache)

  * [Sample Code](https://api-docs.deepseek.com/guides/function_calling#sample-code)



WeChat Official Account

  * ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)



Community

  * [Email](mailto:api-service@deepseek.com)
  * [Discord](https://discord.gg/Tc7c45Zzu5)
  * [Twitter](https://twitter.com/deepseek_ai)



More

  * [GitHub](https://github.com/deepseek-ai)



Copyright Â© 2024 DeepSeek, Inc.
