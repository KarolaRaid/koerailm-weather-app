import requests
from django.shortcuts import render



def index(request):
    # Placeholder for now. Eventually use user's real location (via IP or browser API) as default
    location = "Tallinn"

    api_url = f"https://whatever-url-for-api.com/API_blabla{location}"
    response = requests.get(api_url)

    context = {}

    if response.status_code == 200:
        weather_data = response.json()


        temp_c = weather_data.get('current', {}).get('temp_c', None)
        condition_text = weather_data.get('current', {}).get('condition', {}).get('text', None)
        wind_kph = weather_data.get('current', {}).get('wind_kph', None)
        humidity = weather_data.get('current', {}).get('humidity', None)



        # Save weather data to the database
        if temp_c is not None and condition_text is not None:
            weather_record = weather_data(
                location_id=location,
                temperature=temp_c,
                humidity=humidity,
                wind_speed=wind_kph,
                condition=condition_text,

            )
            weather_record.save()

        context['weather_data'] = weather_data
    else:
        context['weather_data'] = "No weather data available"

    return render(request, 'weather_data.html', context)



