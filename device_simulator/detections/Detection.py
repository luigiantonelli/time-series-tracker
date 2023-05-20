import logging
import time


class Detection:
    def __init__(self, class_name):
        self.log = logging.getLogger(class_name)

    def get(self):
        pass


class DetectionInstance:
    def __init__(self):
        self.timestamp = time.time_ns()

    pass
