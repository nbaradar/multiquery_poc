# File: multiquery/llm_providers/grok.py

from .base import LLMProvider

class GrokProvider(LLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
 
    def send_query(self, query: str) -> str:
        return f"Mock response from Grok for query: '{query}'"
