from .base import BaseAIProvider
from .gemini import GeminiService

def create_ai_provider(provider: str) -> BaseAIProvider:
    providers = {
        "gemini": GeminiService,
    }

    try:
        provider_class = providers[provider]
    except KeyError:
        raise ValueError(f"Unknown AI provider: {provider}")

    return provider_class()