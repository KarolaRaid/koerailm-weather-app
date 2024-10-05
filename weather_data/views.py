import requests
from django.shortcuts import render


def index(request):
    # Placeholder for now. Eventually use user's real location (via IP or browser API) as default
    location = "Tallinn"

    api_url = f"https://whatever-url-for-api.com/API_blabla{location}"
    response = requests.get(api_url)

    context = {}
    if response.status_code == 200:
        weather_data = response.json()
        context['weather_data'] = weather_data
    context['weather_data'] = "No weather data available"
    return render(request, 'weather_data.html', context)


