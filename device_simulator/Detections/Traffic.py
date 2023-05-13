import json
import random
import time

ids = [1,2,3,4,5]
locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']
speeds = [s for s in range(0, 300)]

class TrafficDetection:
    def __init__(self, id, location, license_plate, speed, timestamp):
        self.id = id
        self.location = location
        self.license_plate = license_plate
        self.speed = speed
        self.timestamp = timestamp

detections = []
for _ in range(5):
    l_p = ''.join(random.choices(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), k=2)) + \
          ''.join(random.choices(list("0123456789"), k=3)) + \
          ''.join(random.choices(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), k=2))
    td = TrafficDetection(random.choices(ids)[0],
                          random.choices(locations)[0],
                          l_p,
                          random.choice(range(0, 300)),
                          time.strftime("%H:%M:%S", time.localtime())
                          )
    detections.append(json.dumps(td.__dict__))

print(detections)