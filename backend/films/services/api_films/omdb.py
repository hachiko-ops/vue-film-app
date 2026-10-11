from .base import BaseFilmsProvider
import requests
from config.settings import OMDB_API_URL,OMDB_API_KEY

class OMDBService(BaseFilmsProvider):

    def find_film(self, title:str) -> dict | None:
        try:
            omdb_response = requests.get(
                    OMDB_API_URL,
                    params={
                        "t": title,
                        "apikey": OMDB_API_KEY
                    },
                    timeout=10,
                )
            
            omdb_response.raise_for_status()
            film_data = omdb_response.json()
            
        except requests.RequestException as e:
            raise ValueError(f"OMDB returned an invalid response: {str(e)}") from e

        if film_data.get("Response") == "False":
            return None
        
        return film_data