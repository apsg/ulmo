#!/usr/bin/python3

# Before usage
# sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
# sudo python3 -m pip install --force-reinstall adafruit-blinka

import os
from time import *

import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 8)

pixels.fill((0,255,0))