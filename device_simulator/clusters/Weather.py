import pandas

import config as config
from clusters.Cluster import Cluster
from detectors.Weather import WeatherDetector


class WeatherCluster(Cluster):
    def __init__(self, c_id, size, loop):
        super().__init__(__name__, c_id, loop, 8080)
        df = pandas.read_csv(config.ITALY_CITIES)
        cities = df.sample(n=size).values.tolist()

        self.log.info(f"init weather cluster with {size} devices")
        for i, city in enumerate(cities):
            d = WeatherDetector(i, city[2], city[3], city[4], city[5])
            self.devices.append(d)
