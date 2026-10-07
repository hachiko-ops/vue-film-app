from django.http import JsonResponse

def search(request):
    if request.method == 'GET':
        search = request.GET.get('s')

    if( search is None or search == ''):
        return JsonResponse({"error": "Search parameter is required"}, status=400)

    if len(search) < 3:
        return JsonResponse({"error": "Search parameter must be at least 3 characters long"}, status=400)

    
    
    # Sample data for demonstration purposes
    films = [
        {"id": 1, "title": "Film 1", "description": "Description of Film 1"},
        {"id": 2, "title": "Film 2", "description": "Description of Film 2"},
        {"id": 3, "title": "Film 3", "description": "Description of Film 3"},
    ]
    return JsonResponse(films, safe=False)
