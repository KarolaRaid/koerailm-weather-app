import requests


API_KEY = 'eb27810bad464fb88ec151353242409'
LOCATION = 'Tallinn'


def fetch_weather_data(location):
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Uh-oh! Looks like we can't fetch the weather right now. Maybe the internet dog chewed the cable?")
        return None


def evaluate_dog_weather(weather_data):
    temp_c = weather_data['current']['temp_c']
    humidity = weather_data['current']['humidity']
    precip_mm = weather_data['current']['precip_mm']
    wind_kph = weather_data['current']['wind_kph']
    condition = weather_data['current']['condition']['text']


    if 5 <= temp_c <= 20 and precip_mm == 0 and wind_kph < 20:
        return f"Paw-some! It's a perfect day for a walk! The weather is {condition} with {temp_c}°C. Grab the leash!"
    elif temp_c < 5:
        return f"Brrr! It's too chilly for most pups out there! Only {temp_c}°C. Maybe time for a snuggle instead?"
    elif temp_c > 25:
        return f"Yikes! It's {temp_c}°C, which is basically a doggy sauna. You don’t want to boil your best buddy!"
    elif precip_mm > 2:
        return f"Rain, rain, go away! With {precip_mm}mm of rain, your dog might end up smelling like wet fur. Maybe save the walk for later?"
    else:
        return f"Hmm... the weather is a bit mixed: {condition} with {temp_c}°C. Could go either way—play it by ear (or by tail wag)."


def main():
    print("Sniffing out the weather for your dog...")
    weather_data = fetch_weather_data(LOCATION)

    if weather_data:
        dog_weather_evaluation = evaluate_dog_weather(weather_data)
        print(dog_weather_evaluation)
    else:
        print("Oops! Couldn't fetch the weather data. Your dog might have to rely on the old-fashioned sniff test.")


if __name__ == '__main__':
    main()
