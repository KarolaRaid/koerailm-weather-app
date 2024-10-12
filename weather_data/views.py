import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from koerailm_weather_app.models import WeatherData
from weather_data.api import get_weather_data, get_weather_data_by_geolocation
from django.views.decorators.csrf import csrf_exempt




def current_weather(request):
    context = {}

    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')


    if latitude and longitude:
        weather_data = get_weather_data_by_geolocation(latitude, longitude)
        location = weather_data.get('location').get('name')
    else:
        location = request.GET.get('location_search') or 'Nice'
        weather_data = get_weather_data(location)
        location = weather_data.get('location').get('name')


    if weather_data:
        #city = weather_data.get('location').get('name')
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

        context['latitude'] = latitude
        context['longitude'] = longitude

        context['dog_rating'] = dog_weather_index(wind_kmh, precipitation)


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
    return condition_text_ee.get(condition_text) if condition_text in condition_text_ee.keys() else condition_text


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


def dog_weather_index(wind_kmh, precipitation):
    """
    Wind Intensity Scale (modified from the Beaufort Wind Scale)
    0 - Bf 0-1, 0-5 km/h
    1 - Bf 2-3, 6-19 km/h
    2 - Bf 4-5, 20-38 km/h
    3 - Bf 6-7, 39-61 km/h
    4 - Bf 8-9, 62-88 km/h
    5 - Bf 10-12, 89+ km/h
    """

    wind_rating = {
        (0, 5.9): 0,
        (6, 19.9): 1,
        (20, 38.9): 2,
        (39, 61.9): 3,
        (62, 88.9): 4,
        (89, 500): 5
    }

    wind_value = None
    for k in wind_rating.keys():
        if k[0] <= wind_kmh <= k[1]:
            wind_value = wind_rating.get(k)

    """
    Rain Intensity Scale (modified from the Meteorological Standard's Rainfall Intensity Classifications)
    0 - 0 mm/h
    1 - <0.5 mm/h
    2 - 0.5-2.5 mm/h
    3 - 2.5-7.5 mm/h
    4 - 7.5-15 mm/h
    5 - 15+ mm/h
    """

    rain_rating = {
        (0, 0.04): 0,
        (0.05, 0.49): 1,
        (0.5, 2.49): 2,
        (2.5, 7.49): 3,
        (7.5, 14.99): 4,
        (15, 500): 5
    }

    rain_value = None
    for k in rain_rating.keys():
        if k[0] <= precipitation <= k[1]:
            rain_value = rain_rating.get(k)

    dog_rating = round((0.25 * wind_value) + (0.75 * rain_value))

    return dog_rating



