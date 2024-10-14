import requests
from decouple import config


def get_weather_data(location, is_estonia):
    api_key = config('WEATHER_API_KEY')
    weather_url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&days=2&q={location}'

    if is_estonia:
        weather_url += ',EE'

    weather_response = requests.get(weather_url)

    if weather_response.status_code == 200:
        return weather_response.json()

    return None


def get_search_location(location_search):
    is_estonia = False
    api_key = config('WEATHER_API_KEY')
    search_url = f'http://api.weatherapi.com/v1/search.json?key={api_key}&q={location_search}'
    search_response = requests.get(search_url)

    if search_response.status_code == 200:
        search_results = search_response.json()

        if len(search_results) > 0:
            preferred_entry = None

            for result in search_results:
                preferred_entry = result

                if "Estonia" == result.get('country'):
                    preferred_entry = result
                    is_estonia = True
                    break

            location_search = preferred_entry.get('name')

        else:
            return {'error': 'Asukohta ei leitud. Palun proovige uuesti.'}
    else:
        return {'error': 'Asukohta ei leitud. Palun proovige uuesti.'}

    return location_search, is_estonia


def get_weather_data_by_geolocation(latitude, longitude):
    lat = round(float(latitude), 4)
    lon = round(float(longitude), 4)

    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat},{lon}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None

