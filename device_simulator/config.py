import logging

# API
OPEN_WEATHER_API_KEY = "dba5689e46a3054dd04647a292ed6a37"
OPEN_WEATHER_API_FORMAT = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
# LOG
LOG_LEVEL = logging.DEBUG
# SLEEP AMONG DETECTIONS
SLEEP_TIME = 1
FETCH_SLEEP_TIME = 60
# TYPES
WEATHER_TYPE = 'weather'
TRAFFIC_TYPE = 'traffic'
ENERGY_TYPE = 'energy'
# PATHS
ITALY_CITIES = "resources/italy.csv"
ITALY_AUTOVELOX = "resources/autovelox_map.json"
ITALY_ENERGY = "resources/electricity_Italy.csv"
