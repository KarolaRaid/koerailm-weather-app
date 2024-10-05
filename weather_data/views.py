from django.shortcuts import render
from django.http import HttpResponse
from koerailm_weather_app.models import WeatherData
from weather_data.api import get_weather_data


# Create your views here.
def index(request):
    weather_data = get_weather_data('Tallinn')
    return HttpResponse(weather_data)
