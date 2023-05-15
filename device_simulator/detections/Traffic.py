import json
import random
import time

ids = [1,2,3,4,5]
locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']
vehicles = ['Car', 'Truck', 'Bus', 'Motorbike']

class TrafficDetection:
    def __init__(self, id, location, license_plate, vehicle, speed, timestamp):
        self.id = id
        self.location = location
        self.license_plate = license_plate
        self.vehicle = vehicle
        self.speed = speed
        self.timestamp = timestamp

def generate_traffic_detection(ids, locations, vehicles):
    l_p = ''.join(random.choices(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), k=2)) + \
          ''.join(random.choices(list("0123456789"), k=3)) + \
          ''.join(random.choices(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), k=2))
    return TrafficDetection(random.choices(ids)[0],
                            random.choices(locations)[0],
                            l_p,
                            random.choices(vehicles)[0],
                            random.choice(range(0, 300)),
                            time.strftime("%a %b %d %H:%M:%S MST %Y", time.localtime())
                            )

detections = []
for _ in range(5):
    td = generate_traffic_detection(ids, locations, vehicles)
    detections.append(json.dumps(td.__dict__))

print(detections)

