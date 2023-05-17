from detections.Detection import Detection, DetectionInstance


class WeatherDetection(Detection):
    def __init__(self, lat, lng, mgr):
        super().__init__(__name__)
        self.lat = lat
        self.lng = lng
        self.mgr = mgr

    def get(self):
        observation = self.mgr.weather_around_coords(self.lat, self.lng, limit=1)[0]
        l = observation.location.name
        w = observation.weather
        t = w.temperature('celsius')
        detection = WeatherDetectionInstance(l, t['temp'], t['feels_like'], w.pressure['press'], w.status)
        self.log.debug(detection.__dict__)
        return detection.__dict__


class WeatherDetectionInstance(DetectionInstance):
    def __init__(self, location, temp, perc_temp, pressure, status):
        super().__init__()
        self.location = location
        self.temp = temp
        self.perc_temp = perc_temp
        self.pressure = pressure
        self.status = status
