import requests
from django.shortcuts import render
from django.utils import timezone  # For timestamp management
from weather_data.api import get_weather_data

from koerailm_weather_app.models import WeatherData


def index(request):
    # Placeholder for now. Eventually use user's real location (via IP or browser API) as default
    location = "Tallinn"

    api_url = f"https://whatever-url-for-api.com/API_blabla{location}"
    response = requests.get(api_url)

    context = {}

    weather_data = get_weather_data(location)

    country = weather_data.get('location').get('country')
    temp_c = weather_data.get('current').get('temp_c')
    condition_text = weather_data.get('current').get('condition').get('text')
    wind_kph = weather_data.get('current').get('wind_kph')
    wind_dir = weather_data.get('current').get('wind_dir')
    precip_mm = weather_data.get('current').get('precip_mm')
    humidity = weather_data.get('current').get('humidity')
    cloud = weather_data.get('current').get('cloud')
    feelslike_c = weather_data.get('current').get('feelslike_c')


    try:
        # (you can modify this if needed)
        location_id = 1


        weather_record = WeatherData(
            location_id=location_id,
            temperature=temp_c,
            humidity=humidity,
            wind_speed=wind_kph,
            condition=condition_text,
            timestamp=timezone.now()
        )
        weather_record.save()

    except Exception as e:
        print(f"Error saving weather data: {e}")


    context['location'] = location
    context['country'] = country
    context['temp_c'] = temp_c
    context['condition_text'] = condition_text
    context['wind_kph'] = wind_kph
    context['wind_dir'] = wind_dir
    context['precip_mm'] = precip_mm
    context['humidity'] = humidity
    context['cloud'] = cloud
    context['feelslike_c'] = feelslike_c

    return render(request, 'index.html', context)


