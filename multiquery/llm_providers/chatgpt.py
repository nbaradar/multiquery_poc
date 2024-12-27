from .base import LLMProvider
from openai import OpenAI
class ChatGPTProvider(LLMProvider):

    def __init__(self, api_key: str):
        self.api_key = api_key

    def send_query(self, query: str) -> str:
        """
        Sends a query to ChatGPT and returns the response.
        """

        #First create a client and set the API key (retrieved from config file)
        client = OpenAI(
            api_key=self.api_key
        )

        #Now attempt to make a call to REST API
        try:
            chat_completion = client.chat.completions.create(
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