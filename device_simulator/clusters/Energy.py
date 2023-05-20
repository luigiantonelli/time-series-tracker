import pandas

import config
from clusters.Cluster import Cluster
from detectors.Energy import EnergyDetector


class EnergyCluster(Cluster):
    def __init__(self, e_id, size, loop):
        super().__init__(__name__, e_id, loop, 8082)
        df = pandas.read_csv(config.ITALY_ENERGY)[['Name', 'Fuel', 'Capacity (MW)']]
        centrals = df.sample(n=size).values.tolist()

        self.log.info(f"init energy cluster with {size} devices")
        for i, c in enumerate(centrals):
            d = EnergyDetector(i, c[0], c[1], c[2])
            self.devices.append(d)
