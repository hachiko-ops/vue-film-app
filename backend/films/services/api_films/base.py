from abc import ABC, abstractmethod

class BaseFilmsProvider(ABC):
    @abstractmethod
    def find_film(self, title:str) -> dict:
        """
        Search for a film by title using an external API.

        Args:
            title (str): The title of the film to search for.

        Returns:
            dict | None: A dictionary containing the film details
                if found, or None if the film does not exist.

        Raises:
            ValueError: If the API request fails or the response
                is invalid.
        """
