import asyncio
import logging
import queue

import config
from detections.Detection import Detection


class Detector:
    def __init__(self, class_name, d_id):
        self.d_id = d_id
        self.log = logging.getLogger(class_name)
        self.log.setLevel(config.LOG_LEVEL)
        self.enable = False
        self.detections = queue.Queue()

    async def start(self):
        self.enable = True
        await self.run()

    async def run(self):
        while self.enable:
            self.log.info(f"detector {self.d_id} generate detection, queue size: {self.detections.qsize()}")
            d = self.get_detection()
            self.detections.put(d)
            await asyncio.sleep(config.SLEEP_TIME)

    def get_detection(self) -> Detection:
        pass

    def stop(self):
        self.log.info(f"stop weather detector with id {self.d_id}")
        self.enable = False

    def get_all_detections(self):
        self.log.info("get all detections from queue")
        res = []
        while self.detections.qsize() > 0:
            res.append(self.detections.get())
        self.log.info(f"fetched {len(res)} detections")
        return res
