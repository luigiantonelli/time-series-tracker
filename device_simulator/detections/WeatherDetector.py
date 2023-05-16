import json
import random
import time
import requests

ids = [1, 2, 3, 4, 5]
weather = ['Sunny', 'Cloudy', 'Rain', 'Storm', 'Hail', 'Snow']
locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']

class WeatherDetection:
    def __init__(self, location, weather, millimeters, temperature, timestamp):
        self.location = location
        self.weather = weather
        self.temperature = temperature
        self.millimeters = millimeters
        self.timestamp = timestamp
