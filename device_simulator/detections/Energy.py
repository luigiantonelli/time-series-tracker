import json
import random
import time

ids = [1,2,3,4,5]
power_stations = ['Solar panel', 'Wind turbine', 'Hydroelectric', 'Gas', 'Carbon', 'Petrol']
locations = ['Bari', 'Firenze', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino']
renewable = set(['Solar panel', 'Wind turbine', 'Hydroelectric'])
fossil = set(['Gas', 'Carbon', 'Petrol'])

class EnergyConsumptionDetection:
    def __init__(self, location, power_stations, consumption, co2_emissions, is_green, timestamp):
        #self.id = id
        self.location = location
        self.consumption = consumption
        self.power_station = power_stations
        self.co2_emissions = co2_emissions
        self.is_green = is_green
        self.timestamp = timestamp

def generate_energy_consumption_detection(locations, power_stations, renewable, fossil):
    consumption = round(random.choice(range(0, 500)) + random.random(), 3)
    ps = random.choices(power_stations)[0]
    if ps in renewable:
        co2_emissions = round(consumption * random.choice(range(1, 2)) * random.random(), 3)
        is_green = True
    elif ps in fossil:
        co2_emissions = round(consumption * random.choice(range(3, 5)) * random.random(), 3)
        is_green = False
        
    return EnergyConsumptionDetection(
                            random.choices(locations)[0],
                            ps,
                            consumption,
                            co2_emissions,
                            is_green,
                            time.time_ns())
"""
detections = []
for _ in range(5):
    ecd = generate_energy_consumption_detection(locations, power_stations, renewable, fossil)
    detections.append(json.dumps(ecd.__dict__))

print(detections)
"""