import pandas

import config
from clusters.Cluster import Cluster
from detectors.Traffic import TrafficDetector


class TrafficCluster(Cluster):
    def __init__(self, c_id, size, loop):
        super().__init__(__name__, c_id, loop)
        df = pandas.read_json(config.ITALY_AUTOVELOX)
        velox = df.sample(n=size).values.tolist()

        self.log.info(f"init traffic cluster with {size} devices")
        for i, v in enumerate(velox):
            d = TrafficDetector(i, v[0], v[2], v[7], v[8])
            self.devices.append(d)
