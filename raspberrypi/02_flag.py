# Author: Mitesh Sharma (mitsharm@redhat.com)
# Name: Simple Fireworks
# Version: 1.0
# Description: Simple firewworks show - raspberrypi
# Program: Python3
# Library: rpi_ws281x


import time
from rpi_ws281x import * 

# LED strip configuration:
LED_COUNT      = 120      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0

def clean(strip):
	for x in range(0, LED_COUNT):
		strip.setPixelColor(x, Color(0,0,0))
	strip.show()

def pole(strip, a, b, c):
	for i in range(0, 59, 1):
		strip.setPixelColor( i , Color(a, b, c))
		for s in range(1,6):
			strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
		strip.show()
		time.sleep(.01)
		strip.setPixelColor( i -7, Color(0,0,0))
		strip.show()

# def pole(strip, a, b, c):
# 	for i in range(0, 59, 1):
# 		strip.setPixelColor( i , Color(a,b,c))
# 		strip.show()

def poleflagpart(strip):
	for saffron in range(60, 69, 1):
		strip.setPixelColor( saffron , Color(255, 165, 0))
		strip.show()
		time.sleep(.2)
	for white in range(69, 79, 1):
		strip.setPixelColor( white , Color(255, 255, 255))
		strip.show()
		time.sleep(.2)
	for green in range(79, 89, 1):
		strip.setPixelColor( green , Color(0, 255, 0))
		strip.show()
		time.sleep(.2)
  
def green(strip, a, b, c):
	for i in range(90, 99, 1):
		strip.setPixelColor( i , Color(a, b, c))
		for s in range(1,3):
			strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
		strip.show()


def white(strip, a, b, c):
	for i in range(99, 109, 1):
		strip.setPixelColor( i , Color(a, b, c))
		for s in range(1,3):
			strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
		strip.show()

  
def saffron(strip, a, b, c):
	for i in range(109, 119, 1):
		strip.setPixelColor( i , Color(a, b, c))
		for s in range(1,3):
			strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
		strip.show()


# Main program logic follows:	
def main():
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()
	print('Press Ctrl-C to quit.')
	while True:
		pole(strip,255, 165, 0)
		clean(strip)
		poleflagpart(strip)
		green(strip,0, 255, 0)
		time.sleep(1)
		white(strip,255, 255, 255)
		time.sleep(1)
		saffron(strip,	255, 165, 0)
		time.sleep(10)
		clean(strip)	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		strip.begin()
		clean(strip)