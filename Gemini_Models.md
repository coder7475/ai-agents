Free access in the Gemini Developer API (“AI Studio” / Gemini API free tier) is available for specific models where the pricing table shows “Free of charge” for Free Tier input/output.[1]

## Models with free tier (common ones)
From Google’s current Gemini API pricing page, these model codes show Free Tier input and output as “Free of charge”: 

- `gemini-3-flash-preview`   
- `gemini-2.5-pro`   
- `gemini-2.5-flash`   
- `gemini-2.5-flash-lite`   
- `gemini-2.0-flash`   
- `gemini-2.0-flash-lite`   
- `gemini-embedding-001` (embeddings; input free tier)   

## Models not free (examples)
These are explicitly marked “Not available” for Free Tier on the same pricing page (paid only): 

- `gemini-3-pro-preview`   
- `gemini-3-pro-image-preview`   
- Imagen 3 / Imagen 4 image-gen models   
- Veo video-gen models   
- `gemini-2.5-computer-use-preview-10-2025`   

## Why you may still see “limit: 0”
Even when a model supports Free Tier pricing, actual availability/rate limits depend on your project’s current usage tier and the rate limits shown in AI Studio (and if you exceed them you’ll get 429s).[1]

If you tell which exact model string you’re calling (you mentioned `gemini-3-pro`), can suggest the closest free-tier equivalent for your use case (coding/reasoning vs speed).

[1](https://github.com/google/adk-python/discussions/3404)
[2](https://ai.google.dev/gemini-api/docs/pricing)
[3](https://blog.laozhang.ai/api-guides/gemini-api-free-tier/)
[4](https://ai.google.dev/gemini-api/docs/models)
[5](https://www.datastudios.org/post/all-gemini-models-available-in-2025-complete-list-for-web-app-api-and-vertex-ai)
[6](https://www.aifreeapi.com/en/posts/gemini-api-free-tier-limit)
[7](https://ai.google.dev/gemini-api/docs/billing)
[8](https://openrouter.ai/google/gemini-2.0-flash-exp:free)
[9](https://www.aifreeapi.com/en/posts/gemini-api-free-quota)
[10](https://www.youtube.com/watch?v=OIPTgnmhFVk)
[11](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash-lite)
[12](https://www.spurnow.com/en/blogs/is-gemini-api-free)
[13](https://developers.google.com/program/plans-and-pricing)
[14](https://developers.googleblog.com/en/gemini-2-family-expands/)
[15](https://www.cursor-ide.com/blog/gemini-2-5-pro-free-api-limits-guide)
[16](https://www.cloudeagle.ai/blogs/blogs-google-gemini-pricing-guide)
[17](https://blog.google/technology/google-deepmind/gemini-model-updates-february-2025/)
[18](https://www.reddit.com/r/GeminiAI/comments/1pg4et5/google_reduces_api_rate_limits_for_free_tier/)
[19](https://www.reddit.com/r/GoogleGeminiAI/comments/1ky3sgg/gemini_api_billing_does_enabling_paid_tier/)
[20](https://cloud.google.com/vertex-ai/generative-ai/pricing)
[21](https://www.cloudzero.com/blog/gemini-pricing/)