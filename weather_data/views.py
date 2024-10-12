from django.shortcuts import render
from weather_data.api import get_weather_data, get_weather_data_by_geolocation
from weather_data.translations import text_condition_trans, wind_direction_trans
from weather_data.dog_weather_index import dog_weather_index


def current_weather(request):
    context = {}

    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    if latitude and longitude:
        weather_data = get_weather_data_by_geolocation(latitude, longitude)
    elif 'location_search' in request.GET:
        weather_data = get_weather_data(request.GET.get('location_search'))
    else:
        weather_data = get_weather_data('Kuressaare')

    location = weather_data.get('location').get('name')

    if weather_data and 'error' in weather_data:
        context['error'] = weather_data['error']
    elif weather_data:
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

    return render(request, 'index.html', context)
