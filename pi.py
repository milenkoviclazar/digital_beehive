"""
read the temperature and humidity from DHT11
"""

import Adafruit_DHT

import datetime

sensor = Adafruit_DHT.DHT11
pin = '4'

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

now = datetime.datetime.now()

if humidity is not None and temperature is not None:
    print('{0:0.1f}* {1:0.1f}% %s %s %s'.format(temperature, humidity, now.hour, now.minute))
