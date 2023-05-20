import random

from detections.Detection import Detection, DetectionInstance


class TrafficDetection(Detection):
    def __init__(self, city, region, lat, lng):
        super().__init__(__name__)
        self.city = city
        self.region = region
        self.lat = lat
        self.lng = lng

    def get(self):
        detection = TrafficDetectionInstance(self.city, self.region, self.lat, self.lng)
        self.log.debug(detection.__dict__)
        return detection.__dict__


def generate_italian_plate():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '0123456789'
    letters = ''
    numbers = ''
    for c in range(4):
        letters += random.choice(chars)
    for c in range(3):
        numbers += random.choice(nums)
    return f"{letters[:2]} {numbers} {letters[-2:]}"


class TrafficDetectionInstance(DetectionInstance):
    def __init__(self, city, region, lat, lng):
        super().__init__()
        self.city = city
        self.region = region
        self.lat = lat
        self.lng = lng
        self.license_plate = generate_italian_plate()
        self.speed = float("{:.2f}".format(random.random() * 200))
