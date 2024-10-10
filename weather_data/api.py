import requests
from decouple import config


def set_location(request):
    location = request.GET.get('location', 'Nice')
    return location

def get_weather_data(location):
    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


