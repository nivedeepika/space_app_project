import requests
from django.http import JsonResponse

NASA_API_KEY = "CMWMxuPUrZIUFgAn3IfqwOU1vprsmCPit86f37KX"  # Replace with your NASA API key
def apod(request):
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)
# Mars Rover Photos with Search
def mars_photos(request):
    search_date = request.GET.get("date")  # Get search date from query params
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    
    if search_date:
        url = f"{base_url}?earth_date={search_date}&api_key={NASA_API_KEY}"
    else:
        url = f"{base_url}?sol=1000&api_key={NASA_API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)
