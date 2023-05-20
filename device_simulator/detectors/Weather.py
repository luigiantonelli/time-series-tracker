from pyowm import OWM

import config
from detections.Detection import Detection
from detections.Weather import WeatherDetection
from detectors.Detector import Detector


class WeatherDetector(Detector):
    def __init__(self, d_id, city, lat, lng, country):
        super().__init__(__name__, d_id)
        self.city = city
        self.lat = lat
        self.lng = lng
        self.country = country

        owm = OWM(config.OPEN_WEATHER_API_KEY)
        self.mgr = owm.weather_manager()

    async def start(self):
        self.log.info(f"start detector with id {self.d_id} locate in {self.city}")
        await super().start()

    def get_detection(self) -> Detection:
        return WeatherDetection(self.lat, self.lng, self.mgr).get()
