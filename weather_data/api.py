import requests
from decouple import config


def get_weather_data(location):
    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    print("Uh-oh! Looks like we can't fetch the weather right now. Maybe the internet dog chewed the cable?")
    return None