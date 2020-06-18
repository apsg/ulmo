#!/usr/bin/python

import sys
from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO  # zaimportuj biblioteke
from time import *

load_dotenv()
pin = int(os.getenv('PIN_WATER'))

GPIO.setmode(GPIO.BCM)  # ustaw tryb na numeracje procesora
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.LOW);
sleep(60)
GPIO.output(pin, GPIO.HIGH);

