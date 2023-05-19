from src.detections.Detection import Detection
from src.detections.Energy import EnergyDetection
from src.detectors.Detector import Detector


class EnergyDetector(Detector):
    def __init__(self, e_id, name, fuel_type, capacity):
        super().__init__(__name__, e_id)
        self.name = name
        self.fuel_type = fuel_type
        self.capacity = capacity

    async def start(self):
        self.log.info(f"start detector with id {self.d_id} with name {self.name} with fuel type {self.fuel_type} and "
                      f"capacity of {self.capacity} (MW)")
        await super().start()

    def get_detection(self) -> Detection:
        return EnergyDetection(self.name, self.fuel_type, self.capacity).get()
