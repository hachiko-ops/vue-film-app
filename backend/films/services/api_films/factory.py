from .base import BaseFilmsProvider
from films.services.api_films.omdb import OMDBService

def create_films_provider(provider: str) -> BaseFilmsProvider:
    providers = {
        "omdb": OMDBService,
    }

    try:
        provider_class = providers[provider]
    except KeyError:
        raise ValueError(f"Unknown API Fims provider: {provider}")

    return provider_class()