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
	for i in range(0, 89, 1):
		strip.setPixelColor( i , Color(a, b, c))
		strip.show()

def white(strip, a, b, c):
	for i in range(90, 99, 1):
		strip.setPixelColor( i , Color(a, b, c))
		strip.show()

def green(strip, a, b, c):
	for i in range(99, 109, 1):
		strip.setPixelColor( i , Color(a, b, c))
		strip.show()
  
def saffron(strip, a, b, c):
	for i in range(109, 119, 1):
		strip.setPixelColor( i , Color(a, b, c))
		strip.show()


# Main program logic follows:	
def main():
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()
	print('Press Ctrl-C to quit.')
	while True:
		pole(strip,x[0],x[1],x[2])
		green(strip,0, 255, 0)
		white(strip,255, 255, 255)
		saffron(strip,244, 196, 48)
		time.sleep(1)
		clean(strip)	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		strip.begin()
		clean(strip)