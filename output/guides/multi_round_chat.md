[Skip to main content](https://api-docs.deepseek.com/guides/multi_round_chat#__docusaurus_skipToContent_fallback)

[![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)**DeepSeek API Docs**](https://api-docs.deepseek.com/)

[ English](https://api-docs.deepseek.com/guides/multi_round_chat)

  * [English](https://api-docs.deepseek.com/guides/multi_round_chat)
  * [ä¸­æï¼ä¸­å½ï¼](https://api-docs.deepseek.com/zh-cn/guides/multi_round_chat)



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
  * Multi-round Conversation



# Multi-round Conversation

This guide will introduce how to use the DeepSeek `/chat/completions` API for multi-turn conversations.

The DeepSeek `/chat/completions` API is a "stateless" API, meaning the server does not record the context of the user's requests. Therefore, the user must **concatenate all previous conversation history** and pass it to the chat API with each request.

The following code in Python demonstrates how to concatenate context to achieve multi-turn conversations.
    
    
    from openai import OpenAI  
    client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")  
      
    # Round 1  
    messages = [{"role": "user", "content": "What's the highest mountain in the world?"}]  
    response = client.chat.completions.create(  
        model="deepseek-chat",  
        messages=messages  
    )  
      
    messages.append(response.choices[0].message)  
    print(f"Messages Round 1: {messages}")  
      
    # Round 2  
    messages.append({"role": "user", "content": "What is the second?"})  
    response = client.chat.completions.create(  
        model="deepseek-chat",  
        messages=messages  
    )  
      
    messages.append(response.choices[0].message)  
    print(f"Messages Round 2: {messages}")  
    

* * *

In the **first round** of the request, the `messages` passed to the API are:
    
    
    [  
        {"role": "user", "content": "What's the highest mountain in the world?"}  
    ]  
    

In the **second round** of the request:

  1. Add the model's output from the first round to the end of the `messages`.
  2. Add the new question to the end of the `messages`.



The `messages` ultimately passed to the API are:
    
    
    [  
        {"role": "user", "content": "What's the highest mountain in the world?"},  
        {"role": "assistant", "content": "The highest mountain in the world is Mount Everest."},  
        {"role": "user", "content": "What is the second?"}  
    ]  
    

[PreviousGet User Balance](https://api-docs.deepseek.com/api/get-user-balance)[NextChat Prefix Completion (Beta)](https://api-docs.deepseek.com/guides/chat_prefix_completion)

WeChat Official Account

  * ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)



Community

  * [Email](mailto:api-service@deepseek.com)
  * [Discord](https://discord.gg/Tc7c45Zzu5)
  * [Twitter](https://twitter.com/deepseek_ai)



More

  * [GitHub](https://github.com/deepseek-ai)



Copyright Â© 2024 DeepSeek, Inc.
