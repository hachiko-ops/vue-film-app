from django.http import JsonResponse
from .services.gemini import GeminiService

def filters(request, session_id=None):
    if( request.method != 'GET'):
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
    search = request.GET.get('s')
    if( search is None or search == ''):
        return JsonResponse({"error": "Search parameter is required"}, status=400)

    if len(search) < 3:
        return JsonResponse({"error": "Search parameter must be at least 3 characters long"}, status=400)

    gemini_service = GeminiService()
    filters = gemini_service.get_films(search, session_id)

    # TODO Check if on OMDB API exists all films suggest from Gemini, if not, remove them from the list otherwise return the list of films found in OMDB API with all details.

    return JsonResponse(filters, safe=False)
