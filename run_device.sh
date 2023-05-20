docker run -d --ip 172.18.0.4 --name=traffic_cluster --net=influxdb --rm detector_simulator -t traffic -s 10 -i 1 -f 10
docker run -d --ip 172.18.0.5 --name=weather_cluster --net=influxdb --rm detector_simulator -t weather -s 10 -i 2 -f 10
docker run -d --ip 172.18.0.6 --name=energy_cluster --net=influxdb --rm detector_simulator -t energy -s 10 -i 3 -f 10