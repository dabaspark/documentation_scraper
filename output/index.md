[Skip to main content](https://api-docs.deepseek.com#__docusaurus_skipToContent_fallback)

[![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)![DeepSeek API Docs Logo](https://cdn.deepseek.com/platform/favicon.png)**DeepSeek API Docs**](https://api-docs.deepseek.com/)

[ English](https://api-docs.deepseek.com)

  * [English](https://api-docs.deepseek.com/)
  * [ä¸­æï¼ä¸­å½ï¼](https://api-docs.deepseek.com/zh-cn/)



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
  * Your First API Call



On this page

# Your First API Call

The DeepSeek API uses an API format compatible with OpenAI. By modifying the configuration, you can use the OpenAI SDK or softwares compatible with the OpenAI API to access the DeepSeek API.

PARAM| VALUE  
---|---  
base_url *âââââââ| `https://api.deepseek.com`  
api_key| apply for an [API key](https://platform.deepseek.com/api_keys)  
  
* To be compatible with OpenAI, you can also use `https://api.deepseek.com/v1` as the `base_url`. But note that the `v1` here has NO relationship with the model's version.

* **The`deepseek-chat` model has been upgraded to DeepSeek-V3. The API remains unchanged.** You can invoke DeepSeek-V3 by specifying `model='deepseek-chat'`.

## Invoke The Chat API[â](https://api-docs.deepseek.com#invoke-the-chat-api "Direct link to Invoke The Chat API")

Once you have obtained an API key, you can access the DeepSeek API using the following example scripts. This is a non-stream example, you can set the `stream` parameter to `true` to get stream response.

  * curl
  * python
  * nodejs


    
    
    curl https://api.deepseek.com/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer <DeepSeek API Key>" \  
      -d '{  
            "model": "deepseek-chat",  
            "messages": [  
              {"role": "system", "content": "You are a helpful assistant."},  
              {"role": "user", "content": "Hello!"}  
            ],  
            "stream": false  
          }'  
    
    
    
    # Please install OpenAI SDK first: `pip3 install openai`  
      
    from openai import OpenAI  
      
    client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")  
      
    response = client.chat.completions.create(  
        model="deepseek-chat",  
        messages=[  
            {"role": "system", "content": "You are a helpful assistant"},  
            {"role": "user", "content": "Hello"},  
        ],  
        stream=False  
    )  
      
    print(response.choices[0].message.content)  
    
    
    
    // Please install OpenAI SDK first: `npm install openai`  
      
    import OpenAI from "openai";  
      
    const openai = new OpenAI({  
            baseURL: 'https://api.deepseek.com',  
            apiKey: '<DeepSeek API Key>'  
    });  
      
    async function main() {  
      const completion = await openai.chat.completions.create({  
        messages: [{ role: "system", content: "You are a helpful assistant." }],  
        model: "deepseek-chat",  
      });  
      
      console.log(completion.choices[0].message.content);  
    }  
      
    main();  
    

[NextModels & Pricing](https://api-docs.deepseek.com/quick_start/pricing)

  * [Invoke The Chat API](https://api-docs.deepseek.com#invoke-the-chat-api)



WeChat Official Account

  * ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)



Community

  * [Email](mailto:api-service@deepseek.com)
  * [Discord](https://discord.gg/Tc7c45Zzu5)
  * [Twitter](https://twitter.com/deepseek_ai)



More

  * [GitHub](https://github.com/deepseek-ai)



Copyright Â© 2024 DeepSeek, Inc.
