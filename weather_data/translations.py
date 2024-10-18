def weekday_convert(isoweekday):
    weekday_ee = {
        1: "Esmaspäev",
        2: "Teisipäev",
        3: "Kolmapäev",
        4: "Neljapäev",
        5: "Reede",
        6: "Laupäev",
        7: "Pühapäev"
    }
    return weekday_ee.get(isoweekday)

def month_convert(month):
    month_ee = {
        1: "jaanuar",
        2: "veebruar",
        3: "märts",
        4: "aprill",
        5: "mai",
        6: "juuni",
        7: "juuli",
        8: "august",
        9: "september",
        10: "oktoober",
        11: "november",
        12: "detsember"
    }
    return month_ee.get(month)


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
