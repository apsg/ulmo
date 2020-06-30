#!/usr/bin/python3

import sys
from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO  # zaimportuj biblioteke
from time import *

load_dotenv()
pin = int(os.getenv('PIN_BLINK'))

GPIO.setmode(GPIO.BCM)  # ustaw tryb na numeracje procesora
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

for i in range(5):
    GPIO.output(pin, GPIO.LOW);
    sleep(0.5)
    GPIO.output(pin, GPIO.HIGH);
    sleep(0.5)

GPIO.output(pin, GPIO.LOW);
