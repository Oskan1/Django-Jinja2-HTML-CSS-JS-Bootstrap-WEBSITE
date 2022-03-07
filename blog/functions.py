import requests
import math

cityy = "Saarbrücken, DE"

listCity = []
listCountry = []
listTemp = []
listFeltTemp = []
listHumidity = []
listWindS = []


def get_weather(api_key):

    lat = [49.233334, 51.509865, 37.983810, 41.01224]
    lon = [7.000000, -0.118092, 23.727539, 28.976018]
    countries = [(49.233334, 7.000000), (51.509865, -0.118092), (37.983810, 23.727539), (41.015137, 28.979530)]

    for latitude, lontitude in countries:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={lontitude}&appid={api_key}"

        response = requests.get(url).json()

        temp2 = response['main']['temp']
        temp = math.floor((temp2 * 1.8) - 459.67) - 35
        listTemp.append(temp)

        feels = response['main']['feels_like']
        feels = math.floor((feels * 1.8) - 459.67) - 35
        listFeltTemp.append(feels)

        humidity = response['main']['humidity']
        listHumidity.append(humidity)

        windspeed = response['wind']['speed']
        listWindS.append(windspeed)

        city2 = response['name']
        listCity.append(city2)

        country = response['sys']['country']
        listCountry.append(country)

    zips = [[x, y, z, a, b, c] for x, y, z, a, b, c in zip(listTemp, listFeltTemp, listHumidity, listWindS, listCity, listCountry)]

    allDict = [
        {'temp': zips[0][0], 'felttemp': zips[0][1], 'humidity': zips[0][2], 'windspeed': zips[0][3], 'city': zips[0][4], 'country': zips[0][5]},
        {'temp': zips[1][0], 'felttemp': zips[1][1], 'humidity': zips[1][2], 'windspeed': zips[1][3], 'city': zips[1][4], 'country': zips[1][5]},
        {'temp': zips[2][0], 'felttemp': zips[2][1], 'humidity': zips[2][2], 'windspeed': zips[2][3], 'city': zips[2][4], 'country': zips[2][5]},
        {'temp': zips[3][0], 'felttemp': zips[3][1], 'humidity': zips[3][2], 'windspeed': zips[3][3], 'city': zips[3][4], 'country': zips[3][5]}
    ]

    countries = ["Germany", "England", "Greece", "Turkey"]

    return allDict


