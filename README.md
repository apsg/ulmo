# [ulmo](http://tolkiengateway.net/wiki/Ulmo)
Python bundle for my raspberry Pi. It steers watering system of my little garden :)
It runs on Raspberry 3B+.

See it here: http://balkon.gackowski.edu.pl

To run it one require to create `.env` file containing config variables.

### Measurements

It gets current temperature and humidity measurements using DHT11 sensor and sends it to external api via POST request.

Usage:

    python3 measurements.py
