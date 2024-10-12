import requests
from decouple import config



def get_weather_data(location):
    api_key = config('WEATHER_API_KEY')

    search_url = f'http://api.weatherapi.com/v1/search.json?key={api_key}&q={location}'
    search_response = requests.get(search_url)

    if search_response.status_code == 200:
        search_results = search_response.json()

        if len(search_results) > 0:
            entry_ee = None
            for entry in search_results:
                if entry['country'] == "Estonia":
                    entry_ee = entry
                    break

            entry_preferred = entry_ee if entry_ee is not None else search_results[0]

            entry_preferred['name'] = location


            weather_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
            weather_response = requests.get(weather_url)
            if weather_response.status_code == 200:
                return weather_response.json()

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


