#! python3
# umbrellaReminder.py - checks if it is raining. If it is, sends a text
# with a reminder to bring an umbrella.
# Requires textMyself.py to be in the cwd.

import json
import requests
import sys
import textMyself

# API key for OpenWeatherMap.org's API
APIkey = 'yourAPIKey'

location = 'yourTownOrCity, gb'

# Download the JSON data from OpenWeatherMap.org's API
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&cnt=3&APPID={APIkey}'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData
if w['weather'][0]['main'] == 'Rain':
    textMyself.textMyself('It\'s raining, man. Hallelujah! Don\'t forget your umbrella!')
