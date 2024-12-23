from .base import LLMProvider

class ChatGPTProvider(LLMProvider):
    """
    Mock implementation for the ChatGPT LLM provider.
    """
    def send_query(self, query: str) -> str:
        return f"Mock response from ChatGPT for query: '{query}'"