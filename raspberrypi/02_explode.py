# Author: Mitesh Sharma (mitsharm@redhat.com)
# Name: Simple Fireworks
# Version: 1.0
# Description: Simple firewworks show - raspberrypi
# Program: Python3
# Library: rpi_ws281x


import time
import random
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 120      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0


sparkPos = []
sparkVel = []
sparkCol = []
gravity = -.0019

for i in range(0, LED_COUNT):
    sparkPos.insert(i, '')
    sparkVel.insert(i, '')
    sparkCol.insert(i, '')


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def clean(strip):
	for x in range(0, LED_COUNT):
		strip.setPixelColor(x, Color(0,0,0))
	strip.show()

def flare(strip, a, b, c):
	for i in range(0, 89, 1):
		strip.setPixelColor( i , Color(a, b, c))
		for s in range(1,6):
			strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
		strip.show()
		time.sleep(.01)
		strip.setPixelColor( i -7, Color(0,0,0))
		strip.show()


def flare1(strip, a, b, c):
    flarePos = 0
    flareVel = float(random.getrandbits(16)) / 90
	# flareVel = float(random16(60, 80)) / 90
    brightness = float(1)
    for i in range(0,5,1):
        sparkPos[i] = 0
        sparkVel[i] = (float(random.getrandbits(8) / 255) * (flareVel / 5))
        sparkCol[i] = sparkVel[i] * 1000
        sparkCol[i] = constrain(sparkCol[i], 0, 255)
    clean(strip)
    while flareVel >= -.05:
        for i in range(0,5,1):
            sparkPos[i] += sparkVel[i]
            sparkPos[i] = constrain(sparkPos[i], 0, 120)
            sparkVel[i] += gravity
            sparkCol[i] += -.8
            sparkCol[i] = constrain(sparkCol[i], 0, 255)
            color_code = ((0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,0,255),(255,250,0),(50,255,255),(255,50,150),(255,250,50))
            for x in color_code:
                flare1(strip,x[0],x[1],x[2])
                # clean(strip)
            # leds[int(sparkPos[i])] = HeatColor(sparkCol[i])
            # leds[int(sparkPos[i])] %= 50;
        strip.setPixelColor(round(flarePos), Color(0,0,round(brightness * 255)))
        strip.show()
        clean(strip)
        flarePos += flareVel
        flareVel += gravity
        brightness *= .99








def burst(strip, a, b, c):
	for i in range(90, 119, 1):
		strip.setPixelColor( i , Color(a, b, c))
		for s in range(1,9):
			strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
		strip.show()
		time.sleep(.01)
		strip.setPixelColor( i -10, Color(0,0,0))
		strip.show()

# Main program logic follows:	
def main():
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()
	print('Press Ctrl-C to quit.')
	color_code = ((0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,0,255),(255,250,0),(50,255,255),(255,50,150),(255,250,50))
	while True:
		for x in color_code:
			flare1(strip,x[0],x[1],x[2])
			clean(strip)
			burst(strip,x[0],x[1],x[2])
			clean(strip)	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		strip.begin()
		clean(strip)