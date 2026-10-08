from urllib import response

from django.http import JsonResponse
from google import genai

def search(request):
    if( request.method != 'GET'):
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
    search = request.GET.get('s')
    if( search is None or search == ''):
        return JsonResponse({"error": "Search parameter is required"}, status=400)

    if len(search) < 3:
        return JsonResponse({"error": "Search parameter must be at least 3 characters long"}, status=400)

    client = genai.Client()

    prompt = f"""
You are a film search query parser.

Your task is to analyze the user's search query and extract any information that can be used to search a film database.

Return a JSON object with exactly these seven fields:
- "title": the film title explicitly mentioned in the query. If no film title is mentioned, return an empty string.
- "genre": the film genre explicitly mentioned in the query. If no genre is mentioned, return an empty string.
- "year": the film release year explicitly mentioned in the query. If no year is mentioned, return an empty string.
- "director": the film director explicitly mentioned in the query. If no director is mentioned, return an empty string.
- "actors": a list of actors explicitly mentioned in the query. If no actors are mentioned, return an empty list.
- "language": the film language explicitly mentioned in the query. If no language is mentioned, return an empty string.
- "reason": a short explanation of how you interpreted the query and which filters you extracted.

Important rules:
- Do not invent information that is not present in the query.
- Do not suggest a film title if the user did not provide one.
- If a field cannot be determined from the query, return an empty string or empty lists.
- Return only the JSON object.
- Do not include Markdonw, explanations, or any test outside the JSON object.

User query:
{search}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return JsonResponse(response.text, safe=False)
