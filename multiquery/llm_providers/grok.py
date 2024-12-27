from .base import LLMProvider
from openai import OpenAI

class GrokProvider(LLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
 
    def send_query(self, query: str) -> str:
        """
        Sends a query to Grok and returns the response.
        """

        #First, create the OpenAI client, ut yse the X-AI API URL
        client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.x.ai/v1"
        )

        #Now attempt to make a call to REST API
        try:
            chat_completion = client.chat.completions.create(
                model="grok-2-1212",
                messages=[
                    {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."},
                    {"role": "user", "content": query},
                ],
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
