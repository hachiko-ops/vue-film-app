from .ai.factory import create_ai_provider
from .api_films.factory import create_films_provider
from ..models import SearchRequest

class FilmSearchService:
    def __init__(self, ai_provider: str='gemini', film_provider: str='omdb'):
        self.ai_service = create_ai_provider(ai_provider)
        self.film_service = create_films_provider(film_provider)

    def search_films(self, search: str, session_id:str = None) -> dict:
        try:
            response = self.ai_service.search_films(search)        
        except Exception as e:
            raise

        films_not_found_count = 0

        response["suggest"]["films"] = []
        for film in response['suggest'].get('titles',[]):
            try:
                check = self.film_service.find_film(film)
            except Exception:
                films_not_found_count += 1

            if check is not None:
                response['suggest']['films'].append(check)
            else:
                films_not_found_count += 1
                

        if session_id is not None:
            request_record = SearchRequest(
                session_id=session_id,
                search_query=search,
                filters=response["suggest"],
                reason=response["reason"],
                suggested_films_count=len(response["suggest"].get("titles", [])),
                films_not_found_count=films_not_found_count
            )
            request_record.save()

        return response["suggest"]
