# Author: Mitesh Sharma (mitsharm@redhat.com)
# Firewworks based on raspberrypi

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

def flare(strip, a, b, c):
	for i in range(0, 89, 1):
		strip.setPixelColor( i , Color(a, b, c))
		for s in range(1,6):
			strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
		strip.show()
		time.sleep(.01)
		strip.setPixelColor( i -7, Color(0,0,0))
		strip.show()

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
			flare(strip,x[0],x[1],x[2])
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