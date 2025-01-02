from .base import LLMProvider
import google.generativeai as genai


class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.provider_name = "Gemini"
 
    async def send_query(self, query: str) -> str:
        """
        Sends a query to Gemini and returns the response.
        """

        #FOR DEVELOPMENT: Check for default API key value
        if (self.api_key == "YOUR_GEMINI_API_KEY"):
            return "Please set your Gemini API key in the config file."
        
        try:
            #Set API Key and model
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")

            #Query Gemini
            response = await model.generate_content_async(query)
            return response.text
        except Exception as e:
            return f"Error: {e}"