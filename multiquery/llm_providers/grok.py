from .base import LLMProvider
from openai import AsyncOpenAI

class GrokProvider(LLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
 
    async def send_query(self, query: str) -> str:
        """
        Sends a query to Grok and returns the response.
        """

        #FOR DEVELOPMENT: Check for default API key value
        if (self.api_key == "YOUR_GROK_API_KEY"):
            return "Please set your Grok API key in the config file."

        #First, create the OpenAI client, ut yse the X-AI API URL
        client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://api.x.ai/v1"
        )

        #Now attempt to make a call to REST API
        try:
            chat_completion = await client.chat.completions.create(
                model="grok-2-1212",
                messages=[
                    {"role": "system", "content": "You are Grok, a chatbot designed by xAI"},
                    {"role": "user", "content": query},
                ],
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
