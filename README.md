# Time-series-tracker
A simple project that collect, aggregate and save detections using influxDB and Telegraf

# Plugins

## input
* https://github.com/influxdata/telegraf/blob/release-1.26/plugins/inputs/http_listener_v2/README.md

## output
* https://github.com/influxdata/telegraf/blob/release-1.26/plugins/outputs/influxdb_v2/README.md

# First Setup

```
cp ${TELEGRAF.CONF_SOURCE_PATH} ${TELEGRAF.CONF_PATH} 
```

```
docker network create influxdb
```

```
docker run -d \
	-p 8080:8080 -p 8081:8081 -p 8082:8082 \
	--name=telegraf \
    --net=influxdb \
    -v ${TELEGRAF.CONF_PATH}/telegraf.conf:/etc/telegraf/telegraf.conf:ro \
    telegraf
```
	  
```	  
docker run -d -p 8086:8086 --name=influxdb \
	--net=influxdb \
	influxdb
```

```
docker run -d \
	--name=traffic_cluster \
    --net=influxdb \
    traffic_simulator
```


# Start

1. `cp ${TELEGRAF.CONF_SOURCE_PATH} ${TELEGRAF.CONF_PATH}`

2. Run influxDB and telegraf container
