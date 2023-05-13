# time-series-tracker
A simple project that collect, aggregate and save detections using influxDb and telegraf

**input**
https://github.com/influxdata/telegraf/blob/release-1.26/plugins/inputs/http_listener_v2/README.md

**output**
https://github.com/influxdata/telegraf/blob/release-1.26/plugins/outputs/influxdb_v2/README.md

**commands**

```
docker run -d --name=telegraf \
      --net=influxdb \
      -v /home/lory271/telegraf.conf:/etc/telegraf/telegraf.conf:ro \
      telegraf
	  
	  
docker run -d --name=influxdb --net=influxdb -p 8086:8086 influxdb
```
