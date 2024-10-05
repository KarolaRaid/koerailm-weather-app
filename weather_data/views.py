import requests
from django.shortcuts import render
from django.http import HttpResponse
from koerailm_weather_app.models import WeatherData
from weather_data.api import get_weather_data



def index(request):
    # Placeholder for now. Eventually use user's real location (via IP or browser API) as default
    location = "Tallinn"
    context = {}
    weather_data = get_weather_data('Tallinn')
    context['weather_data'] = weather_data
    return render(request, 'weather_data.html', context)


