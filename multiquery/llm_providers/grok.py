# File: multiquery/llm_providers/grok.py

from .base import LLMProvider

class GrokProvider(LLMProvider):
    """
    Mock implementation for the Grok LLM provider.
    """
    def send_query(self, query: str) -> str:
        return f"Mock response from Grok for query: '{query}'"
