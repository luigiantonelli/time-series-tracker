import asyncio
import logging
import sys

import config
from clusters.Traffic import TrafficCluster

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=config.LOG_LEVEL)
    logger = logging.getLogger(__name__)
    logger.setLevel(config.LOG_LEVEL)
    print("ciao")
    logger.info("loop not created")
    loop = asyncio.get_event_loop()
    logger.debug("loop created")
    cluster = TrafficCluster(1, 2, loop)
    loop.run_until_complete(cluster.start())
    loop.close()
    # df = pandas.read_json("resources/autovelox_map.json")
    # df = df.sample(n=3).values.tolist()
    # print(df)
