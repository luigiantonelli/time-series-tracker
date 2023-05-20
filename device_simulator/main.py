import argparse
import asyncio
import logging
import sys

import config
from clusters.Energy import EnergyCluster
from clusters.Traffic import TrafficCluster
from clusters.Weather import WeatherCluster

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='detectors_simulator.', add_help=True)
    parser.add_argument('-t', action='store', choices=['traffic', 'energy', 'weather'], dest='type', required=True,
                        help='choose the cluster type')
    parser.add_argument('-s', action='store', required=True, default=3, type=int, dest='size',
                        help='choose the cluster size')
    parser.add_argument('-i', action='store', required=True, default=1, type=int, dest='id',
                        help='choose the cluster id')
    parser.add_argument('-f', action='store', required=True, default=60, type=int, dest='send_time',
                        help='choose the send time jitter')
    parser.add_argument('--seed', action='store', required=True, default=0, type=int, dest='seed',
                        help='choose seed to sample cluster')
    TYPE = parser.parse_args().type
    SIZE = parser.parse_args().size
    ID = parser.parse_args().id
    config.FETCH_SLEEP_TIME = parser.parse_args().send_time
    config.SEED = parser.parse_args().seed

    logging.basicConfig(stream=sys.stdout, level=config.LOG_LEVEL)
    logger = logging.getLogger(__name__)

    loop = asyncio.get_event_loop()
    logger.debug("loop created")

    if TYPE == config.WEATHER_TYPE:
        cluster = WeatherCluster(ID, SIZE, loop)
    elif TYPE == config.TRAFFIC_TYPE:
        cluster = TrafficCluster(ID, SIZE, loop)
    else:
        cluster = EnergyCluster(ID, SIZE, loop)

    loop.run_until_complete(cluster.start())
    loop.close()
