from detections.Detection import Detection
from detections.Traffic import TrafficDetection
from detectors.Detector import Detector


class TrafficDetector(Detector):
    def __init__(self, d_id, city, region, lat, lng):
        super().__init__(__name__, d_id)
        self.city = city
        self.region = region
        self.lat = lat
        self.lng = lng

    async def start(self):
        self.log.info(f"start detector with id {self.d_id} locate in {self.city} - {self.region}")
        await super().start()

    def get_detection(self) -> Detection:
        return TrafficDetection(self.city, self.region, self.lat, self.lng).get()
