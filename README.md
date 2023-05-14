# time-series-tracker
A simple project that collects, aggregates and saves detections using InfluxDb and Telegraf

**input**
https://github.com/influxdata/telegraf/blob/release-1.26/plugins/inputs/http_listener_v2/README.md

**output**
https://github.com/influxdata/telegraf/blob/release-1.26/plugins/outputs/influxdb_v2/README.md

**commands**

```
docker run -d -p 8080:8080 --name=telegraf \
      --net=influxdb \
      -v /home/lory271/telegraf.conf:/etc/telegraf/telegraf.conf:ro \
      telegraf
	  
	  
docker run -d --name=influxdb --net=influxdb -p 8086:8086 influxdb
```
