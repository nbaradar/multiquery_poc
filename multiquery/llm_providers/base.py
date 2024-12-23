from abc import ABC, abstractmethod

class LLMProvider(ABC):
    """
    Base class for LLM providers
    """

    @abstractmethod
    def send_query(self, query: str) -> str:
        """
        Sends a query to the LLM and returns the response.
        Must be implemented by subclasses.
        """
        pass