import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from koerailm_weather_app.models import WeatherData
from weather_data.api import get_weather_data, set_location



def current_weather(request):
    context = {}
    # Placeholder for now. Eventually use user's real location (via IP or browser API) as default or search result
    #location = set_location()
    location = request.GET.get('location_search', 'Nice')
    weather_data = get_weather_data(location)

    country = weather_data.get('location').get('country')
    temperature = weather_data.get('current').get('temp_c')
    condition_text = weather_data.get('current').get('condition').get('text')
    wind = weather_data.get('current').get('wind_kph')
    wind_direction = weather_data.get('current').get('wind_dir')
    precipitation = weather_data.get('current').get('precip_mm')
    humidity = weather_data.get('current').get('humidity')
    cloud = weather_data.get('current').get('cloud')
    temperature_feelslike = weather_data.get('current').get('feelslike_c')
    icon = weather_data.get('current').get('condition').get('icon')

    # condition_text + wind_dir need to be translated (simple dictionary)
    context['location'] = location
    context['country'] = country
    context['temperature'] = temperature
    context['condition_text'] = condition_text
    context['wind'] = wind
    context['wind_direction'] = wind_direction
    context['precipitation'] = precipitation
    context['humidity'] = humidity
    context['cloud'] = cloud
    context['temperature_feelslike'] = temperature_feelslike
    context['icon'] = icon

    return render(request, 'index.html', context)


#def location_search(request, location_input):
#    return HttpResponseRedirect(f'/{location_input}/')

