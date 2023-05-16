import asyncio
import json
import logging
import time
from datetime import datetime

import requests
import pandas

import config
from clusters.Weather import WeatherCluster
from detections.Weather import WeatherDetection

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(level=config.LOG_LEVEL)
    logger = logging.getLogger(__name__)
    logger.setLevel(config.LOG_LEVEL)
    # print_hi('PyCharm')
    # ids = [1, 2, 3, 4, 5]
    # weather = ['Sunny', 'Cloudy', 'Rain', 'Storm', 'Hail', 'Snow']
    # locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']
    # detections = []
    # for _ in range(5):
    #     wsd = generate_weather_station_detection(locations, weather).__dict__
    #     detections.append(wsd)
    #
    # headers = {"Content-Type": "application/json"}
    #
    # url = "http://localhost:8080/telegraf"
    #
    # # Send the data via HTTP POST request
    # response = requests.post(url, headers=headers, json=detections)
    #
    # # Check the response status code
    # print(f"body: {detections}")
    # print(f"response: {response}")
    # c = pandas.read_csv(config.ITALY_CITIES)
    # s = c.sample(n=3).values.tolist()
    # for ci in s:
    #     print(ci[1])
    print("ciao")
    logger.info("loop not created")
    loop = asyncio.get_event_loop()
    logger.debug("loop created")
    cluster = WeatherCluster(1, 2, loop)
    loop.run_until_complete(cluster.start())
    loop.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
