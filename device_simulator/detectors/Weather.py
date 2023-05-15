import json
import random
import time
import requests

ids = [1, 2, 3, 4, 5]
weather = ['Sunny', 'Cloudy', 'Rain', 'Storm', 'Hail', 'Snow']
locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']

class WeatherDetector:
    def __init__(self, id, position):
        self.id = id
        self.position = position

    def start(self, locations, weather):
        prob = 0.2
        if(random.random() < prob):
            print("generateee")
        l = random.choices(locations)[0]
        if l in set(['Bari', 'Palermo', 'Napoli']):
            w = random.choices(['Sunny', 'Cloudy', 'Rain', 'Storm', 'Hail'])[0]
        else:
            w = random.choices(weather)[0]
        if w in set(['Rain', 'Storm', 'Hail', 'Snow']):
            mm = round(random.choice(range(0, 10)) + random.random(), 3)
        else:
            mm = 0
        if w in set(['Rain', 'Storm']):
            t = round(random.choice(range(5, 40)) + random.random(), 3)
        elif w == 'Hail':
            t = round(random.choice(range(1, 15)) + random.random(), 3)
        elif w == 'Snow':
            t = round(random.choice(range(-15, 0)) + random.random(), 3)
        else:
            t = round(random.choice(range(-15, 40)) + random.random(), 3)
        return WeatherDetector(l,
                               w,
                               mm,
                               t,
                               time.time_ns()
                               )
