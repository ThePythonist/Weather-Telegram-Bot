import requests
from datetime import datetime
from queries import *


def normalizer(timestamp=None, kelvin=None):
    date = str(datetime.fromtimestamp(timestamp))
    temp = kelvin - 273.15
    return {"date": date, "temp": temp}


def get_weather_data(city):
    try:
        key = "646c4e5be6f1f78a1fe101e266ec7bc5"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        PARAMS = {'q': city, 'appid': key}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        normalized_data = normalizer(kelvin=data['main']['temp'], timestamp=data['dt'] + 12600)
        city = data['name']
        date = normalized_data["date"]
        temp = normalized_data["temp"]
        hum = data['main']['humidity']
        save_data_in_db(city, date, temp, hum)
        return {"temp": temp, "hum": hum, "date": date, "name": city, "error": None}
    except Exception as error:
        return {"temp": None, "hum": None, "date": None, "name": "Incorrect City Name", "error": error}

# get_weather_data("Tehran")
# check_db("tehran")
