import time

from pyowm.weatherapi25.observation import Observation
from pyowm.weatherapi25.weather import Weather
from pyowm.weatherapi25.location import Location

from detections.Detection import Detection, DetectionInstance
import logging


class WeatherDetection(Detection):
    def __init__(self, lat, lng, mgr):
        self.lat = lat
        self.lng = lng
        self.mgr = mgr
        self.log = logging.getLogger(__name__)

    def get_detection(self):
        observation = self.mgr.weather_around_coords(self.lat, self.lng, limit=1)[0]
        l = observation.location.name
        w = observation.weather
        t = w.temperature('celsius')
        detection = WeatherDetectionInstance(l, t['temp'], t['feels_like'], w.pressure['press'], w.status)
        self.log.debug(detection.__dict__)
        return detection.__dict__


class WeatherDetectionInstance(DetectionInstance):
    def __init__(self, location, temp, perc_temp, pressure, status):
        self.location = location
        self.temp = temp
        self.perc_temp = perc_temp
        self.temp_diff = round(temp - perc_temp, 2)
        self.pressure = pressure
        self.status = status
        self.timestamp = time.time_ns()
