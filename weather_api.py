import os
import requests
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')

def main():
    lat_lon = get_coordinates()
    pprint(f'COORDINTATES: {lat_lon}')
    weather_data, error = get_weather(lat_lon, key)

    if error:
        print('Sorry, could not get weather')
    else:
        current_temp = get_weather_information(weather_data)
        print(f'The current temperature is {current_temp}')
        

def get_coordinates():
    city, country = '', ''
    # error handling -- catching empty strings; make sure user enters a value
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()
    while len(country) == 0:
        country = input('Enter the two letter code of a country: ')
    if country == 'US':
        state = input('Enter the two letter code of a state: ')
        us_location = f'{city},{state},{country}'

    location = f'{city},{country}'

    geocode_api_url = 'http://api.openweathermap.org/geo/1.0/direct'

    try:
        if country == 'US':
            query = {'q': us_location, 'limit': 1, 'appid': key}
            response = requests.get(geocode_api_url, params=query)
            response.raise_for_status()  # error handling, check for 400 & 500 errors
            coordinate_data = response.json()
            return coordinate_data, None # return none if this errors
        else:
            query = {'q': location, 'appid': key}
            response = requests.get(geocode_api_url, params=query)

            response.raise_for_status()  # error handling, check for 400 & 500 errors
            coordinate_data = response.json()

            latitude = coordinate_data['lat']
            longitude = coordinate_data['lon']

            return latitude, longitude, None # return none if this errors

    except Exception as ex:
        print(ex)
        print(response.text) # for debugging
        return None, ex


def get_weather(lat_long, key):
    url = f'https://api.openweathermap.org/data/2.5/weather'
    query = {'q': 'minneapolis', 'units': 'imperial', 'appid':key}
    try:
        query = {'lat': lat_long[0], 'lon': lat_long[1], 'cnt': 5, 'units': 'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status() # raie exception for 400 or 500 errors
        data = response.json() # this may error too, if response is not JSON
        return data, None # will return none if this errors
    except Exception as ex:
        print(ex)
        print(response.text) # added for debugging
        return None, ex


def get_weather_information(weather_data):

    list_of_forecasts = weather_data['list'] # drill down into the list to be iterated over

    for forecast_information in list_of_forecasts:
        temp = forecast_information['temp']
        weather_description = forecast_information['weather']['description']
        wind_speed = forecast_information['speed']

        timestamp = forecast_information['dt']
        forecast_time = datetime.fromtimestamp(timestamp) # use datetime to pull the time from the time in the API

    forecast_printed_info = f'At {forecast_time} it will be {temp}F, and the weather will be {weather_description}, and the wind speed will be {wind_speed}.'
    return forecast_printed_info


if __name__ == '__main__':
    main()