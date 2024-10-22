from datetime import datetime
from django.shortcuts import render
from weather_data.api import get_weather_data, get_weather_data_by_geolocation, get_search_location
from weather_data.translations import text_condition_trans, wind_direction_trans
from weather_data.dog_weather_index import dog_weather_index
from koerailm_weather_app.models import FolkSaying
from weather_data.dates import date_today


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

        context['date_today'] = date_today()

        context['dog_rating'] = dog_weather_index(wind_kmh, precipitation)

        current_month = datetime.now().month
        current_folk_saying = FolkSaying.objects.filter(month__month=current_month).first()
        context['current_folk_saying'] = current_folk_saying

        current_hour_index = 0
        current_hour_value = None

        # Getting the index of current hour for all hourly calculations
        for i in weather_data.get('forecast').get('forecastday')[0].get('hour'):
            if int(i.get('time')[11:13]) == datetime.now().hour:
                current_hour_value = i.get('time')[11:13]
                break
            else:
                current_hour_index += 1
        context['current_hour_value'] = current_hour_value

        hourly_weather_data = []
        context['hourly_weather_data'] = hourly_weather_data

        for offset in range(0, 8):
            index = current_hour_index + offset

            forecastday_index = index // 24
            hour_index_within_day = index % 24

            hour_data = weather_data.get('forecast').get('forecastday')[forecastday_index]. \
                get('hour')[hour_index_within_day]
            hourly_weather_data.append({
                'h_hour': hour_data.get('time')[11:16],
                'h_temperature': hour_data.get('temp_c'),
                'h_icon': hour_data.get('condition').get('icon'),
                'h_dog_rating': dog_weather_index(hour_data.get('wind_kph'),
                                                  hour_data.get('precip_mm'))
            })

    return render(request, 'index.html', context)
