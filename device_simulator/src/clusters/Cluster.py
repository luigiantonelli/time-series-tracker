import asyncio
import logging

import requests

from src import config


class Cluster:
    def __init__(self, class_name, c_id, loop, port=8080):
        self.c_id = c_id
        self.loop = loop
        self.port = port
        self.log = logging.getLogger(class_name)
        self.log.setLevel(config.LOG_LEVEL)
        self.devices = []

    async def start(self):
        self.log.info(f"start cluster {self.c_id}")
        tasks = []
        for dev in self.devices:
            self.log.debug(f"cluster start device {dev.d_id}")
            tasks.append(self.loop.create_task(dev.start()))
            tasks.append(self.loop.create_task(self.send()))
        await asyncio.wait(tasks)

    async def send(self):
        self.log.info(f"sending detections...")
        while True:
            for dev in self.devices:
                self.send_to_telegraf(dev.get_all_detections())
            await asyncio.sleep(config.FETCH_SLEEP_TIME)

    def send_to_telegraf(self, detections):
        self.log.info(f"{len(detections)} detections sent to telegraf")
        headers = {"Content-Type": "application/json"}
        url = f"http://localhost:{self.port}/telegraf"
        # Send the data via HTTP POST request
        try:
            response = requests.post(url, headers=headers, json=detections)
        except requests.exceptions.RequestException as e:
            self.log.debug(f"request raise an exception {e}")
            return
        self.log.debug(response.status_code)

    def stop(self):
        self.log.info(f"stop cluster")
        for dev in self.devices:
            dev.stop()
