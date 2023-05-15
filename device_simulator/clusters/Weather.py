import json
import random
import time
import requests

ids = [1, 2, 3, 4, 5]
weather = ['Sunny', 'Cloudy', 'Rain', 'Storm', 'Hail', 'Snow']
locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']

class WeatherCluster:
    def __init__(self, id, position):
        self.id = id
        self.position = position
