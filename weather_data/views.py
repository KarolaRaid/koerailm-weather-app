import requests
from django.shortcuts import render
from django.http import HttpResponse
from koerailm_weather_app.models import WeatherData
from weather_data.api import get_weather_data



def index(request):
    # Placeholder for now. Eventually use user's real location (via IP or browser API) as default
    context = {}
    location = 'Tallinn'
    weather_data = get_weather_data(location)
    current_temperature = weather_data.get('current').get('temp_c')
    context['location'] = location
    context['current_temperature'] = current_temperature
    return render(request, 'index.html', context)


