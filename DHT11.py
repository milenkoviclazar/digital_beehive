#!/usr/bin/python

"""
read the temperature and humidity from DHT11
"""

import Adafruit_DHT

import datetime

sensor = Adafruit_DHT.DHT11
pin = '4'

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

now = datetime.datetime.now()

if humidity is not None and temperature is not None:
    print('{:0.1f}* {:0.1f}% {:d} {:d}'.format(temperature, humidity, now.hour, now.minute))
