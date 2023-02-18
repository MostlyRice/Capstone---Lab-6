import os
import requests
from pprint import pprint
from datetime import datetime

# Get the API key from an environment variable
key = os.environ.get('WEATHER_KEY')

def main():
    # Get the latitude and longitude for the location entered by the user
    lat_lon = get_coordinates()

    # Print the coordinates for debugging purposes
    pprint(f'COORDINTATES: {lat_lon}')

    # Get the weather data for the given coordinates
    weather_data, error = get_weather(lat_lon, key)

    # If there was an error getting the weather data, print an error message
    if error:
        print('Sorry, could not get weather')
    else:
        # Print the current temperature
        current_temp = get_weather_information(weather_data)
        print(f'The current temperature is {current_temp}')

# This function gets the coordinates (latitude and longitude) for a given location
def get_coordinates():
    city, country = '', ''

    # Prompt the user to enter the name of a city and the two-letter code for a country
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) == 0:
        country = input('Enter the two letter code of a country: ')

    # If the country is the US, prompt the user to enter the two-letter code for a state
    if country == 'US':
        state = input('Enter the two letter code of a state: ')
        us_location = f'{city},{state},{country}'
    
    # Build the location string for the API query
    location = f'{city},{country}'

    # Set the URL for the geocoding API
    geocode_api_url = 'http://api.openweathermap.org/geo/1.0/direct'

    try:
        # If the country is the US, use the US location string for the API query
        if country == 'US':
            query = {'q': us_location, 'limit': 1, 'appid': key}
            response = requests.get(geocode_api_url, params=query)

            # Check for 400 and 500 errors
            response.raise_for_status()
            
            # Get the coordinate data from the API response
            coordinate_data = response.json()

            # Return the coordinate data and no error
            return coordinate_data, None

        # If the country is not the US, use the regular location string for the API query
        else:
            query = {'q': location, 'appid': key}
            response = requests.get(geocode_api_url, params=query)

            # Check for 400 and 500 errors
            response.raise_for_status()

            # Get the coordinate data from the API response
            coordinate_data = response.json()

            # Get the latitude and longitude from the coordinate data
            latitude = coordinate_data['lat']
            longitude = coordinate_data['lon']

            # Return the latitude and longitude and no error
            return latitude, longitude, None

    # If there was an exception, print the exception and the response text for debugging purposes
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex

# This function gets the weather data for a given set of coordinates
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