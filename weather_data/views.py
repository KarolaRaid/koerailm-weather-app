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
    wind_kmh = weather_data.get('current').get('wind_kph')
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
    context['condition_text'] = text_condition_trans(condition_text)
    context['wind_kmh'] = wind_kmh
    context['wind_ms'] = round(1000 * wind_kmh / 3600, 1)
    context['wind_direction'] = wind_direction_trans(wind_direction)
    context['precipitation'] = precipitation
    context['humidity'] = humidity
    context['cloud'] = cloud
    context['temperature_feelslike'] = temperature_feelslike
    context['icon'] = icon

    return render(request, 'index.html', context)


#def location_search(request, location_input):
#    return HttpResponseRedirect(f'/{location_input}/')


def text_condition_trans(condition_text):
    condition_text_ee = {
        "Sunny": "Päikeseline",
        "Clear": "Selge",
        "Partly cloudy": "Kohati pilvine",
        "Cloudy": "Pilvine",
        "Overcast": "Pilvkate",
        "Mist": "Kerge udu",
        "Patchy rain possible": "Kohati võimalik vihm",
        "Patchy snow possible": "Kohati võimalik lumi",
        "Patchy sleet possible": "Kohati võimalik lörts",
        "Patchy freezing drizzle possible": "Kohati võimalik jäätuv uduvihm",
        "Thundery outbreaks possible": "Võimalikud äikesepuhangud",
        "Blowing snow": "Tuisk",
        "Blizzard": "Lumetorm",
        "Fog": "Udu",
        "Freezing fog": "Jäätuv udu",
        "Patchy light drizzle": "Kohati nõrk uduvihm",
        "Light drizzle": "Nõrk uduvihm",
        "Freezing drizzle": "Jäätuv uduvihm",
        "Heavy freezing drizzle": "Tugev jäätuv uduvihm",
        "Patchy light rain": "Kohati nõrk vihm",
        "Light rain": "Nõrk vihm",
        "Moderate rain at times": "Vahelduvalt mõõdukas vihm",
        "Moderate rain": "Mõõdukas vihm",
        "Heavy rain at times": "Vahelduvalt tugev vihm",
        "Heavy rain": "Tugev vihm",
        "Light freezing rain": "Nõrk jäätuv vihm",
        "Moderate or heavy freezing rain": "Mõõdukas või tugev jäätuv vihm",
        "Light sleet": "Nõrk lörts",
        "Moderate or heavy sleet": "Mõõdukas või tugev lörts",
        "Patchy light snow": "Kohati nõrk lumi",
        "Light snow": "Nõrk lumi",
        "Patchy moderate snow": "Kohati mõõdukas lumi",
        "Moderate snow": "Mõõdukas lumi",
        "Patchy heavy snow": "Kohati tugev lumi",
        "Heavy snow": "Tugev lumi",
        "Ice pellets": "Rahe",
        "Light rain shower": "Nõrk vihmahoog",
        "Moderate or heavy rain shower": "Mõõdukas või tugev vihmahoog",
        "Torrential rain shower": "Paduvihmahoog",
        "Light sleet showers": "Nõrgad lörtsihood",
        "Moderate or heavy sleet showers": "Mõõdukad või tugevad lörtsihood",
        "Light snow showers": "Nõrgad lumesajud",
        "Moderate or heavy snow showers": "Mõõdukad või tugevad lumesajud",
        "Light showers of ice pellets": "Nõrgad rahesajud",
        "Moderate or heavy showers of ice pellets": "Mõõdukad või tugevad rahesajud",
        "Patchy light rain with thunder": "Kohati nõrk vihm äikesega",
        "Moderate or heavy rain with thunder": "Mõõdukas või tugev vihm äikesega",
        "Patchy light snow with thunder": "Kohati nõrk lumi äikesega",
        "Moderate or heavy snow with thunder": "Mõõdukas või tugev lumi äikesega"
    }
    return condition_text_ee.get(condition_text)


def wind_direction_trans(wind_direction):
    wind_direction_ee = {
        "N": "põhjatuul (N)",
        "NNE": "põhja-kirdetuul (NNE)",
        "NE": "kirdetuul (NE)",
        "ENE": "ida-kirdetuul (ENE)",
        "E": "idatuul (E)",
        "ESE": "ida-kagutuul (ESE)",
        "SE": "kagutuul (SE)",
        "SSE": "lõuna-kagutuul (SSE)",
        "S": "lõunatuul (S)",
        "SSW": "lõuna-edelatuul (SSW)",
        "SW": "edelatuul (SW)",
        "WSW": "lääne-edelatuul (WSW)",
        "W": "läänetuul (W)",
        "WNW": "lääne-loodetuul (WNW)",
        "NW": "loodetuul (NW)",
        "NNW": "põhja-loodetuul (NNW)"
    }
    return wind_direction_ee.get(wind_direction)
