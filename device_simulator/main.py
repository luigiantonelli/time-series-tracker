import json

import requests

import Detections
from Detections.Weather import generate_weather_station_detection


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
        wsd = generate_weather_station_detection(ids, locations, weather)
        detections.append(json.dumps(wsd.__dict__))

    url = "http://localhost:8080/telegraf"

    # Send the data via HTTP POST request
    response = requests.post(url, data=detections[0])

    # Check the response status code
    print(response)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
