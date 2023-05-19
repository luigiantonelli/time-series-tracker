import random

from detections.Detection import Detection, DetectionInstance


class EnergyDetection(Detection):
    def __init__(self, name, fuel_type, capacity):
        super().__init__(__name__)
        self.name = name
        self.fuel_type = fuel_type
        self.capacity = capacity

    def get(self):
        detection = EnergyDetectionInstance(self.name, self.fuel_type, self.capacity)
        self.log.debug(detection.__dict__)
        return detection.__dict__


class EnergyDetectionInstance(DetectionInstance):
    def __init__(self, name, fuel_type, capacity):
        super().__init__()
        self.name = name
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.current_load = float("{:.2f}".format(random.random() * capacity))
