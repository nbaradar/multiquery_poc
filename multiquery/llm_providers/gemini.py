from .base import LLMProvider
import google.generativeai as genai


class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
 
    def send_query(self, query: str) -> str:
        """
        Sends a query to Gemini and returns the response.
        """
        try:
            #Set API Key and model
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")

            #Query Gemini
            response = model.generate_content(query)
            return response.text
        except Exception as e:
            return f"Error: {e}"