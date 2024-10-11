import requests
from decouple import config


def get_weather_data(location):
    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_weather_data_by_geolocation(latitude, longitude):
    lat = round(float(latitude), 4)
    lon = round(float(longitude), 4)

    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


