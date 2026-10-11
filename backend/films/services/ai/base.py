from abc import ABC, abstractmethod

class BaseAIProvider(ABC):
    @abstractmethod
    def search_films(self, search: str) -> dict:
        """
        Abstract method to search for films based on a query string.

        Args:
            search (str): The search query string.
            session_id (str, optional): An optional session ID for tracking the request.
        Returns:
            dict: A dictionary containing the search results with the following keys:
                - suggest: A dictionary containing the suggested films and their details, including:
                    - titles: list of candidate film titles (3 to 10).
                    - genre: the genre of the film.
                    - year: the release year of the film.
                    - director: the director of the film.
                    - actors: list of main actors in the film.
                    - "language": the language of the film.
                    - "suggest": a suggestion for a similar film.
                - "reason": a brief explanation of why the film was suggested.
                
        Raises:
            ValueError: If the response from the AI model is not valid JSON or does not contain the expected fields.
        """