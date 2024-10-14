from datetime import datetime
from django.shortcuts import render
from weather_data.api import get_weather_data, get_weather_data_by_geolocation, get_search_location
from weather_data.translations import text_condition_trans, wind_direction_trans
from weather_data.dog_weather_index import dog_weather_index
from koerailm_weather_app.models import FolkSaying


def current_weather(request):
    global weather_data, location
    context = {}

    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    context['error'] = None

    if latitude and longitude:
        weather_data = get_weather_data_by_geolocation(latitude, longitude)
        location = weather_data.get('location').get('name')

    elif request.GET.get('location_search'):
        if 'error' in get_search_location(request.GET.get('location_search')):
            context['error'] = get_search_location(request.GET.get('location_search'))['error']

        else:
            location_search, is_estonia = get_search_location(request.GET.get('location_search'))
            location = location_search
            weather_data = get_weather_data(location, is_estonia)

    else:
        location = 'Stockholm'
        is_estonia = False
        weather_data = get_weather_data(location, is_estonia)

    if context['error'] is None:
        country = weather_data.get('location').get('country')
        temperature = weather_data.get('current').get('temp_c')
        condition_text = weather_data.get('current').get('condition').get('text')
        wind_kmh = weather_data.get('current').get('wind_kph')
        wind_direction = weather_data.get('current').get('wind_dir')
        precipitation = weather_data.get('current').get('precip_mm')
        humidity = weather_data.get('current').get('humidity')
        cloud = weather_data.get('current').get('cloud')
        temperature_feelslike = weather_data.get('current').get('feelslike_c')
        icon = weather_data.get('current').get('condition').get('icon')
        latitude = latitude
        longitude = longitude

        context['location'] = location
        context['country'] = country
        context['temperature'] = temperature
        context['condition_text'] = text_condition_trans(condition_text)
        context['wind_kmh'] = wind_kmh
        context['wind_ms'] = round(1000 * wind_kmh / 3600, 1)
        context['wind_direction'] = wind_direction_trans(wind_direction)
        context['precipitation'] = precipitation
        context['humidity'] = humidity
        context['cloud'] = cloud
        context['temperature_feelslike'] = temperature_feelslike
        context['icon'] = icon

        context['latitude'] = latitude
        context['longitude'] = longitude

        context['dog_rating'] = dog_weather_index(wind_kmh, precipitation)

        current_month = datetime.now().month
        current_folk_saying = FolkSaying.objects.filter(month__month=current_month).first()
        context['current_folk_saying'] = current_folk_saying

    return render(request, 'index.html', context)
