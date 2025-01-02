from .base import LLMProvider
from openai import OpenAI
from openai import AsyncOpenAI
import aiohttp
class ChatGPTProvider(LLMProvider):

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.provider_name = "ChatGPT"

    async def send_query(self, query: str) -> str:
        """
        Sends a query to ChatGPT and returns the response.
        """

        #FOR DEVELOPMENT: Check for default API key value
        #TODO return a more descriptive error message      
        if (self.api_key == "YOUR_CHATGPT_API_KEY"):
            return "Please set your ChatGPT API key in the config file."

        #First create a client and set the API key (retrieved from config file)
        client = AsyncOpenAI(
            api_key=self.api_key
        )

        #Now attempt to make a call to REST API
        try:
            chat_completion = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                    "role": "user",
                    "content": query,
                    },
                ],
                temperature=0.7,  # Adjust for creativity
                max_tokens=150,   # Limit response length
            )
            return chat_completion.choices[0].message.content
        except Exception as e: 
            return f"Error: {e}"