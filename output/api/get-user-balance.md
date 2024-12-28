[Skip to main content](https://api-docs.deepseek.com/api/get-user-balance#__docusaurus_skipToContent_fallback)

[![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)**DeepSeek API Docs**](https://api-docs.deepseek.com/)

[ English](https://api-docs.deepseek.com/api/get-user-balance)

  * [English](https://api-docs.deepseek.com/api/get-user-balance)
  * [ä¸­æï¼ä¸­å½ï¼](https://api-docs.deepseek.com/zh-cn/api/get-user-balance)



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

    * [Introduction](https://api-docs.deepseek.com/api/deepseek-api)
    * [Chat](https://api-docs.deepseek.com/api/create-chat-completion)

    * [Completions](https://api-docs.deepseek.com/api/create-completion)

    * [Models](https://api-docs.deepseek.com/api/list-models)

    * [Others](https://api-docs.deepseek.com/api/get-user-balance)

      * [Get User Balance](https://api-docs.deepseek.com/api/get-user-balance)
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
  * API Reference
  * Others
  * Get User Balance



# Get User Balance
    
    
    GET 
    
    ## /user/balance

Get user current balance

## Responses[â](https://api-docs.deepseek.com/api/get-user-balance#responses "Direct link to Responses")

  * 200



OK, returns user balance info.

  * application/json



  * Schema
  * Example (from schema)
  * Example



**

Schema

**

**is_available** boolean

Whether the user's balance is sufficient for API calls.

**

balance_infos

**

object[]

  * Array [

**currency** string

**Possible values:** [`CNY`, `USD`]

The currency of the balance.

**total_balance** string

The total available balance, including the granted balance and the topped-up balance.

**granted_balance** string

The total not expired granted balance.

**topped_up_balance** string

The total topped-up balance.

  * ]



    
    
    {  
      "is_available": true,  
      "balance_infos": [  
        {  
          "currency": "CNY",  
          "total_balance": "110.00",  
          "granted_balance": "10.00",  
          "topped_up_balance": "100.00"  
        }  
      ]  
    }  
    
    
    
    {  
      "is_available": true,  
      "balance_infos": [  
        {  
          "currency": "CNY",  
          "total_balance": "110.00",  
          "granted_balance": "10.00",  
          "topped_up_balance": "100.00"  
        }  
      ]  
    }  
    

Loading...

[PreviousLists Models](https://api-docs.deepseek.com/api/list-models)[NextMulti-round Conversation](https://api-docs.deepseek.com/guides/multi_round_chat)

WeChat Official Account

  * ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)



Community

  * [Email](mailto:api-service@deepseek.com)
  * [Discord](https://discord.gg/Tc7c45Zzu5)
  * [Twitter](https://twitter.com/deepseek_ai)



More

  * [GitHub](https://github.com/deepseek-ai)



Copyright Â© 2024 DeepSeek, Inc.
