import requests
from django.shortcuts import render
from django.http import HttpResponse
from koerailm_weather_app.models import WeatherData
from weather_data.api import get_weather_data



def index(request):
    context = {}
    # Placeholder for now. Eventually use user's real location (via IP or browser API) as default or search result
    location = 'Tallinn'
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

    # condition_text + wind_dir need to be translated (simple dictionary)
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


