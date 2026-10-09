import json

from django.http import JsonResponse
from google import genai
from google.genai import types
from .models import SearchRequest

def filters(request, session_id=None):
    if( request.method != 'GET'):
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
    search = request.GET.get('s')
    if( search is None or search == ''):
        return JsonResponse({"error": "Search parameter is required"}, status=400)

    if len(search) < 3:
        return JsonResponse({"error": "Search parameter must be at least 3 characters long"}, status=400)

    geminiPrompt = f"""
You are a film search query parser and film recommendation assistant.

Analyze the user's query and extract the available search criteria. 
You must also recommend candidate film titles whenever the user describes a film preference, mood, genre, audience, or theme.

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

    try:
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=geminiPrompt,
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
                )
            )
        )

        response = json.loads(response.text)

    except (json.JSONDecodeError, TypeError) as e:
        return JsonResponse({"error": "Invalid JSON response from Gemini"}, status=502)
    except Exception as e:
        return JsonResponse({"error": f"Unable to process the search request: {str(e)}"}, status=500)

    reason = response.get("reason") or (f'Not found reason in response for query: {search}')

    filters = {
        key: response.get(key)
        for key in ["titles", "genre", "year", "director", "actors", "language", "reason", "suggest"]
    }

    if session_id is not None:
        request_record = SearchRequest(
            session_id=session_id,
            search_query=search,
            filters=filters,
            reason=reason
        )
        request_record.save()

    # TODO Check if on OMDB API exists all films suggest from Gemini, if not, remove them from the list otherwise return the list of films found in OMDB API with all details.

    return JsonResponse(filters, safe=False)
