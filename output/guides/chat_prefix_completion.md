[Skip to main content](https://api-docs.deepseek.com/guides/chat_prefix_completion#__docusaurus_skipToContent_fallback)

[![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)**DeepSeek API Docs**](https://api-docs.deepseek.com/)

[ English](https://api-docs.deepseek.com/guides/chat_prefix_completion)

  * [English](https://api-docs.deepseek.com/guides/chat_prefix_completion)
  * [ä¸­æï¼ä¸­å½ï¼](https://api-docs.deepseek.com/zh-cn/guides/chat_prefix_completion)



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
  * Chat Prefix Completion (Beta)



On this page

# Chat Prefix Completion (Beta)

The chat prefix completion follows the [Chat Completion API](https://api-docs.deepseek.com/api/create-chat-completion), where users provide an assistant's prefix message for the model to complete the rest of the message.

## Notice[â](https://api-docs.deepseek.com/guides/chat_prefix_completion#notice "Direct link to Notice")

  1. When using chat prefix completion, users must ensure that the `role` of the last message in the `messages` list is `assistant` and set the `prefix` parameter of the last message to `True`.
  2. The user needs to set `base_url="https://api.deepseek.com/beta"` to enable the Beta feature.



## Sample Code[â](https://api-docs.deepseek.com/guides/chat_prefix_completion#sample-code "Direct link to Sample Code")

Below is a complete Python code example for chat prefix completion. In this example, we set the prefix message of the `assistant` to `"```python\n"` to force the model to output Python code, and set the `stop` parameter to `['```']` to prevent additional explanations from the model.
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="<your api key>",  
        base_url="https://api.deepseek.com/beta",  
    )  
      
    messages = [  
        {"role": "user", "content": "Please write quick sort code"},  
        {"role": "assistant", "content": "```python\n", "prefix": True}  
    ]  
    response = client.chat.completions.create(  
        model="deepseek-chat",  
        messages=messages,  
        stop=["```"],  
    )  
    print(response.choices[0].message.content)  
    

[PreviousMulti-round Conversation](https://api-docs.deepseek.com/guides/multi_round_chat)[NextFIM Completion (Beta)](https://api-docs.deepseek.com/guides/fim_completion)

  * [Notice](https://api-docs.deepseek.com/guides/chat_prefix_completion#notice)
  * [Sample Code](https://api-docs.deepseek.com/guides/chat_prefix_completion#sample-code)



WeChat Official Account

  * ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)



Community

  * [Email](mailto:api-service@deepseek.com)
  * [Discord](https://discord.gg/Tc7c45Zzu5)
  * [Twitter](https://twitter.com/deepseek_ai)



More

  * [GitHub](https://github.com/deepseek-ai)



Copyright Â© 2024 DeepSeek, Inc.
