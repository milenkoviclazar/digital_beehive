#!/usr/bin/python

"""
read the temperature and humidity from DHT11
"""

import Adafruit_DHT

import datetime

sensor = Adafruit_DHT.DHT11
pin = '4'

average_humidity = 0
average_temperature = 0
n_measurements = 5
for i in range(n_measurements):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    average_humidity += humidity
    average_temperature += temperature
average_temperature /= n_measurements
average_humidity /= n_measurements

now = datetime.datetime.now()

if humidity is not None and temperature is not None:
    print('{:0.1f}* {:0.1f}% {:d} {:d} {:d} {:d} {:d}'.format(average_temperature, average_humidity, now.year, now.month, now.day, now.hour, now.minute))
