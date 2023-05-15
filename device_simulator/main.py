import json
import time
from datetime import datetime

import requests

from detections.MyClass import MyClass
from detections.Weather import generate_weather_station_detection
from detections.Weather import WeatherDetection


# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    ids = [1, 2, 3, 4, 5]
    weather = ['Sunny', 'Cloudy', 'Rain', 'Storm', 'Hail', 'Snow']
    locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']
    detections = []
    for _ in range(5):
        wsd = generate_weather_station_detection(locations, weather).__dict__
        detections.append(wsd)

    headers = {"Content-Type": "application/json"}

    url = "http://localhost:8080/telegraf"

    # Send the data via HTTP POST request
    response = requests.post(url, headers=headers, json=detections)

    # Check the response status code
    print(f"body: {detections}")
    print(f"response: {response}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
