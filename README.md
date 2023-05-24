# Time-series-tracker
A simple project that collect, aggregate and save detections using influxDB and Telegraf

# Plugins

## input
* https://github.com/influxdata/telegraf/blob/release-1.26/plugins/inputs/http_listener_v2/README.md

## output
* https://github.com/influxdata/telegraf/blob/release-1.26/plugins/outputs/influxdb_v2/README.md

# First Setup

Copy telegraf.conf file in the shared volume

```
cp ${TELEGRAF.CONF_SOURCE_PATH} ${TELEGRAF.CONF_PATH} 
```

Create docker subnet for containers

```
docker network create influxdb
```
Build the detector simulator docker image

```
cd ${ROOT_PATH_DEVICE_SIMULATOR}
docker build --tag detector_simulator .
```

Build the notification server docker image

```
cd ${ROOT_PATH_NOTIFICATION_SERVER}
docker build --tag notification_server .
```

Run all!

```
docker run -d \
	-p 8080:8080 -p 8081:8081 -p 8082:8082 \
	--ip 172.18.0.3 \
	--name=telegraf \
    --net=influxdb \
    -v /home/lory271/telegraf.conf:/etc/telegraf/telegraf.conf:ro \
    telegraf
```
	  
```	  
docker run -d -p 8086:8086 --name=influxdb \
	--ip 172.18.0.2 \
	--net=influxdb \
	influxdb
```
```
docker run -d \
	--ip 172.18.0.7 \
	--name=notification_server \
    --net=influxdb \
    --rm notification_server
```

```
docker run -d \
	--ip 172.18.0.4 \
	--name=traffic_cluster \
    --net=influxdb \
    --rm detector_simulator -t traffic -s 10 -i 1 -f 10 --seed 1
```

```
docker run -d \
	--ip 172.18.0.5 \
	--name=weather_cluster \
    --net=influxdb \
    --rm detector_simulator -t weather -s 10 -i 2 -f 10 --seed 1
```

```
docker run -d \
	--ip 172.18.0.6 \
	--name=energy_cluster \
    --net=influxdb \
    --rm detector_simulator -t energy -s 10 -i 3 -f 10 --seed 1
```


# Start

1. `cp ${TELEGRAF.CONF_SOURCE_PATH} ${TELEGRAF.CONF_PATH}`

2. Run all the containers from Docker Desktop

3. execute `run_device.sh`

[Slides] (https://docs.google.com/presentation/d/1vnn5tetHZTvpu_tdt6H-GustGaU1aAaP10g2sR9FOPs/edit#slide=id.g2495b4ad3f5_0_25)
