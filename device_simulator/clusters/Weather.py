import asyncio

import requests

import config
from clusters.Cluster import Cluster
from detectors.Weather import WeatherDetector
import pandas
import logging


class WeatherCluster(Cluster):
    def __init__(self, id, size, loop):
        self.id = id
        self.loop = loop
        self.log = logging.getLogger(__name__)
        self.log.setLevel(config.LOG_LEVEL)
        self.devices = []
        df = pandas.read_csv(config.ITALY_CITIES)
        cities = df.sample(n=size).values.tolist()

        self.log.info(f"init weather cluster with {size} devices")
        for i, city in enumerate(cities):
            d = WeatherDetector(i, city[2], city[3], city[4], city[5])
            self.devices.append(d)

    async def start(self):
        self.log.info("start weather cluster")
        tasks = []
        for dev in self.devices:
            self.log.debug(f"cluster start device {dev.id}")
            tasks.append(self.loop.create_task(dev.start()))
            tasks.append(self.loop.create_task(self.flush()))
        await asyncio.wait(tasks)

    async def flush(self):
        while True:
            for dev in self.devices:
                self.send_to_telegraf(dev.get_all_detections())
            await asyncio.sleep(config.FETCH_SLEEP_TIME)

    def send_to_telegraf(self, detections):
        self.log.info(f"sending {len(detections)} detections to telegraf...")
        headers = {"Content-Type": "application/json"}
        url = "http://localhost:8080/telegraf"
        # Send the data via HTTP POST request
        response = requests.post(url, headers=headers, json=detections)
        self.log.debug(response.status_code)

    def stop(self):
        self.log.info("stop weather cluster")
        for dev in self.devices:
            dev.stop()

