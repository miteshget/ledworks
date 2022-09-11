# Author: Mitesh Sharma (mitsharm@redhat.com)
# Name: WS281b IC LED Turn Off
# Version: 1.0
# Description: Turn off addressable LED strip - raspberrypi
# Program: Python3
# Library: rpi_ws281x

from rpi_ws281x import * 
import time

LED_COUNT = 300
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT,LED_PIN, LED_FREQ_HZ,LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

for x in range(0, LED_COUNT):
  strip.setPixelColor(x, Color(0,0,0))
strip.show()
