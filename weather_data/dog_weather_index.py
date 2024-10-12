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
