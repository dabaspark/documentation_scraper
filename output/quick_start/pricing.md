[Skip to main content](https://api-docs.deepseek.com/quick_start/pricing#__docusaurus_skipToContent_fallback)

[![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)**DeepSeek API Docs**](https://api-docs.deepseek.com/)

[ English](https://api-docs.deepseek.com/quick_start/pricing)

  * [English](https://api-docs.deepseek.com/quick_start/pricing)
  * [ä¸­æï¼ä¸­å½ï¼](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)



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
  * Models & Pricing



On this page

# Models & Pricing

The prices listed below are in unites of per 1M tokens. A token, the smallest unit of text that the model recognizes, can be a word, a number, or even a punctuation mark. We will bill based on the total number of input and output tokens by the model.

## Pricing Details[â](https://api-docs.deepseek.com/quick_start/pricing#pricing-details "Direct link to Pricing Details")

  * USD
  * CNY



Â Â Â Â Â Â MODEL(1)Â Â Â Â Â Â | CONTEXT LENGTH| MAX OUTPUT TOKENS(2)| INPUT PRICE (CACHE HIT)(3)| INPUT PRICE (CACHE MISS)| Â Â OUTPUTÂ PRICEÂ Â Â Â Â   
---|---|---|---|---|---  
deepseek-chat| 64K| 8K| ~~$0.07/ 1M tokens~~(4)  
$0.014 / 1M tokens| ~~$0.27/ 1M tokens~~(4)  
$0.14 / 1M tokens| ~~$1.10/ 1M tokens~~(4)  
$0.28/1M tokens  
  
Â Â Â Â Â Â MODEL(1)Â Â Â Â Â Â | CONTEXT LENGTH| MAX OUTPUT TOKENS(2)| INPUT PRICE (CACHE HIT) (3)| INPUT PRICE (CACHE MISS)| Â Â OUTPUTÂ PRICEÂ Â   
---|---|---|---|---|---  
deepseek-chat| 64K| 8K| ~~Â¥0.5 / 1M tokens~~(4)  
Â¥0.1 / 1M tokens| ~~Â¥2 / 1M tokens~~(4)  
Â¥1 / 1M tokens| ~~Â¥8 / 1M tokens~~(4)  
Â¥2 / 1M tokens  
  
  * (1) **The`deepseek-chat` model has been upgraded to DeepSeek-V3.**
  * (2) If max_tokens is not specified, the default maximum output length is 4K. Please adjust `max_tokens` to support longer outputs.
  * (3) Please check [this article](https://api-docs.deepseek.com/news/news0802) for the details of Context Caching.
  * (4) The form shows the the original price and the discounted price. **From now until 2025-02-08 16:00 (UTC), all users can enjoy the discounted prices of DeepSeek API.** After that, it will recover to full price.



## Deduction Rules[â](https://api-docs.deepseek.com/quick_start/pricing#deduction-rules "Direct link to Deduction Rules")

The expense = number of tokens Ã price. The corresponding fees will be directly deducted from your topped-up balance or granted balance, with a preference for using the granted balance first when both balances are available.

Product prices may vary and DeepSeek reserves the right to adjust them. We recommend topping up based on your actual usage and regularly checking this page for the most recent pricing information.

[PreviousYour First API Call](https://api-docs.deepseek.com/)[NextThe Temperature Parameter](https://api-docs.deepseek.com/quick_start/parameter_settings)

  * [Pricing Details](https://api-docs.deepseek.com/quick_start/pricing#pricing-details)
  * [Deduction Rules](https://api-docs.deepseek.com/quick_start/pricing#deduction-rules)



WeChat Official Account

  * ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)



Community

  * [Email](mailto:api-service@deepseek.com)
  * [Discord](https://discord.gg/Tc7c45Zzu5)
  * [Twitter](https://twitter.com/deepseek_ai)



More

  * [GitHub](https://github.com/deepseek-ai)



Copyright Â© 2024 DeepSeek, Inc.
