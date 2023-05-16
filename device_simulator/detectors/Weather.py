import time
import asyncio
import config
from detections.Weather import WeatherDetection
from detectors.Detector import Detector
import logging
import queue
from pyowm import OWM
from pyowm.utils import timestamps


class WeatherDetector(Detector):
    def __init__(self, id, city, lat, lng, country):
        self.id = id
        self.city = city
        self.lat = lat
        self.lng = lng
        self.country = country

        self.log = logging.getLogger(__name__)
        self.log.setLevel(config.LOG_LEVEL)
        self.enable = False
        self.detections = queue.Queue()

        owm = OWM(config.OPEN_WEATHER_API_KEY)
        self.mgr = owm.weather_manager()

    async def start(self):
        self.log.info(f"start weather detector with id {self.id} locate in {self.city}")
        self.enable = True
        await self.run()

    async def run(self):
        while self.enable:
            self.log.info(f"detector {self.id} generate weather detection, queue size: {self.detections.qsize()}")
            d = WeatherDetection(self.lat, self.lng, self.mgr).get_detection()
            self.detections.put(d)
            await asyncio.sleep(config.SLEEP_TIME)

    def stop(self):
        self.log.info(f"stop weather detector with id {self.id}")
        self.enable = False

    def get_all_detections(self):
        self.log.info("get all detections from queue")
        res = []
        while self.detections.qsize() > 0:
            res.append(self.detections.get())
        self.log.info(f"fetched {len(res)} detections")
        return res
