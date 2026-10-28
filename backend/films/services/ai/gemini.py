import json

from google import genai
from .base import BaseAIProvider
from google.genai import types
from ..api_films.factory import create_films_provider

class GeminiService(BaseAIProvider):
    """
    Abstracts the AI provider and normalizes its output into a
    consistent structure for the application.

    This makes it possible to replace or extend the AI provider
    without changing the view or the rest of the application.
    """

    def __init__(self, film_provider: str='omdb'):
        self.client = genai.Client()
        self.film_service = create_films_provider(film_provider)

    def search_films(self, search: str) -> dict:

        gemini_prompt = f"""
You are a movie recommendation assistant.

When the user asks for movie recommendations:
1. Identify suitable candidate movies.
2. Use the available movie search tool to verify candidates against the OMDb database.
3. Base your final recommendations on the movies actually found.
4. Do not claim that a movie was found unless the tool confirms it.
5. Return the results in the required JSON format.

Return a JSON object with exactly these eight fields:

- "titles": a list of 3 to 10 candidate film titles that could match the user's preferences. If the user does not mention a specific title, actively recommend suitable films based on your general film knowledge. Do not return an empty list just because the user has not provided a title. Return an empty list only if the request does not concern finding or recommending films.
- "genre": the film genre explicitly mentioned in the query. If no genre is mentioned, return an empty string.
- "year": the film release year explicitly mentioned in the query. If no year is mentioned, return an empty string.
- "director": the film director explicitly mentioned in the query. If no director is mentioned, return an empty string.
- "actors": a list of actors explicitly mentioned in the query. If no actors are mentioned, return an empty list.
- "language": the film language explicitly mentioned in the query. If no language is mentioned, return an empty string.
- "reason": a short explanation of how you interpreted the query and which filters you extracted.
- "suggest": a short, natural-language question to ask the user if the query is ambiguous or lacks sufficient information to identify the intended search. If the query is clear enough to proceed, return an empty string.

Important rules:
- Recommend real films that you know are likely to match the user's preferences.
- Suggested titles are candidates, not verified database results. They will be checked against a film database separately.
- Extract search filters only from information explicitly stated by the user. Do not confuse inferred preferences with explicit filters.
- Do not ask for clarification merely because optional search filters are missing.
- Return only valid JSON, with exactly the eight fields specified above.
- Use the correct data types: strings for genre, year, director, language, reason, and suggest; arrays of strings for titles and actors.
- Never replace "titles" with "title" or any other field name. Always use the plural form "titles" for the list of candidate film titles.
- Do not include any additional fields or metadata in the JSON response. Only return the specified eight fields.

User query:
{search}
    """
        
        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=gemini_prompt,
            config=types.GenerateContentConfig(          
                response_mime_type="application/json",
                response_schema=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "titles": {"type": 'ARRAY', "items": {"type": 'STRING'}},
                        "genre": {"type": 'STRING'},
                        "year": {"type": 'STRING'},
                        "director": {"type": 'STRING'},
                        "actors": {"type": 'ARRAY', "items": {"type": 'STRING'}},
                        "language": {"type": 'STRING'},
                        "reason": {"type": 'STRING'},
                        "suggest": {"type": 'STRING'}
                    },
                    required=[
                        "titles",
                        "genre",
                        "year",
                        "director",
                        "actors",
                        "language",
                        "reason",
                        "suggest",
                    ], 
                ),
                tools=[self.verify_film]
            )
        )

        try: 
            response = json.loads(response.text)
        except (json.JSONDecodeError, TypeError) as e:
            raise ValueError(f"Gemini returned an invalid JSON response: {str(e)}") from e
        
        reason = response.get("reason") or (f'Not found reason in response for query: {search}')
            
        suggest = {
            key: response.get(key)
            for key in ["titles", "genre", "year", "director", "actors", "language", "reason", "suggest"]
        }

        return { "suggest": suggest, "reason": reason }

    def verify_film(self, title:str) -> dict:
        """Search for a movie by title in the REST database."""
        print(f"TOOL CALLED: find_film_db({title})")

        try:
            film = self.film_service.find_film(title)
        except Exception as e:
            return {"found": None, "error": str(e), "title": title}

        if film is None:
            return {"found": False, "title": title }

        keys = ["year","director","genre"]
        return {
            "found": True,
            "title": film.get("Title",title),
            **{
                key.lower(): value
                for key, value in film.items()
                if key.lower() in keys
            }
        }    