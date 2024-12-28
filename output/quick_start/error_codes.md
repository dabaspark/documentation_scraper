[Skip to main content](https://api-docs.deepseek.com/quick_start/error_codes#__docusaurus_skipToContent_fallback)

[![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)**DeepSeek API Docs**](https://api-docs.deepseek.com/)

[ English](https://api-docs.deepseek.com/quick_start/error_codes)

  * [English](https://api-docs.deepseek.com/quick_start/error_codes)
  * [ä¸­æï¼ä¸­å½ï¼](https://api-docs.deepseek.com/zh-cn/quick_start/error_codes)



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
  * Quick Start
  * Error Codes



# Error Codes

When calling DeepSeek API, you may encounter errors. Here list the causes and solutions.

Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â CODEÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â | DESCRIPTION  
---|---  
400Â -Â InvalidÂ Format| **Cause** : Invalid request body format.   
**Solution** : Please modify your request body according to the hints in the error message. For more API format details, please refer to [DeepSeek API Docs.](https://api-docs.deepseek.com)  
401Â -Â AuthenticationÂ Fails| **Cause** : Authentication fails due to the wrong API key.   
**Solution** : Please check your API key. If you don't have one, please [create an API key](https://platform.deepseek.com/api_keys) first.  
402Â -Â InsufficientÂ Balance| **Cause** : You have run out of balance.   
**Solution** : Please check your account's balance, and go to the [Top up](https://platform.deepseek.com/top_up) page to add funds.  
422Â -Â InvalidÂ Parameters| **Cause** : Your request contains invalid parameters.   
**Solution** : Please modify your request parameters according to the hints in the error message. For more API format details, please refer to [DeepSeek API Docs.](https://api-docs.deepseek.com)  
429Â -Â RateÂ LimitÂ Reached| **Cause** : You are sending requests too quickly.   
**Solution** : Please pace your requests reasonably. We also advise users to temporarily switch to the APIs of alternative LLM service providers, like OpenAI.  
500Â -Â ServerÂ Error| **Cause** : Our server encounters an issue.   
**Solution** : Please retry your request after a brief wait and contact us if the issue persists.  
503Â -Â ServerÂ Overloaded| **Cause** : The server is overloaded due to high traffic.   
**Solution** : Please retry your request after a brief wait.  
  
[PreviousRate Limit](https://api-docs.deepseek.com/quick_start/rate_limit)[Nextð Introducing DeepSeek-V3](https://api-docs.deepseek.com/news/news1226)

WeChat Official Account

  * ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)



Community

  * [Email](mailto:api-service@deepseek.com)
  * [Discord](https://discord.gg/Tc7c45Zzu5)
  * [Twitter](https://twitter.com/deepseek_ai)



More

  * [GitHub](https://github.com/deepseek-ai)



Copyright Â© 2024 DeepSeek, Inc.
