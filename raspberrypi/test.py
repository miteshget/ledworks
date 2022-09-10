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


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def fireworks(strip, a, b, c):
	for i in range(7, 89, 1):
		strip.setPixelColor( i , Color(a, b, c))
		s_color = round(a * .7),round( b * .7 ),round(c * .7)
		print(s_color)
		strip.setPixelColor( i - 1, Color(s_color[0], s_color[1], s_color[2]))
		# strip.setPixelColor( i - 2, Color(round(a * .7 * .7), round(b * .7 * .7, round(c * .7 * .7))
		# strip.setPixelColor( i - 3, Color(round(a * .7 * .7 * .7, round(b * .7 * .7 * .7, round(c * .7 * .7 * .7))
		# strip.setPixelColor( i - 4, Color(round(a * .7 * .7 * .7 * .7, round(b * .7 * .7 * .7 * .7, round(c * .7 * .7 * .7 * .7))
		# strip.setPixelColor( i - 5, Color(round(a * .7 * .7 * .7 * .7 * .7, round(b * .7 * .7 * .7 * .7 * .7, round(c * .7 * .7 * .7 * .7 * .7))
		# strip.setPixelColor( i - 6, Color(round(a * .7 * .7 * .7 * .7 * .7 * .7, round(b * .7 * .7 * .7 * .7 * .7 * .7, round(c * .7 * .7 * .7 * .7 * .7 * .7))
		strip.show()
		strip.setPixelColor( i -7, Color(0,0,0))
		strip.show()



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print('Press Ctrl-C to quit.')
	while True:
		fireworks(strip, 0, 0, 255)
		fireworks(strip, 0, 255, 0)
		fireworks(strip, 255, 0, 0)
		fireworks(strip, 0, 255, 255)
		fireworks(strip, 255, 0, 255)
		fireworks(strip, 255, 250, 0)
		fireworks(strip, 50, 255, 255)
		fireworks(strip, 255, 50, 150)
		fireworks(strip, 255, 250, 50)

		# colorWipe(strip, Color(255, 0, 0))  # Red wipe
		# colorWipe(strip, Color(0, 255, 0))  # Blue wipe
		# colorWipe(strip, Color(0, 0, 255))  # Green wipe
		# colorWipe(strip, Color(127, 127, 127))  # White theater chase
		# colorWipe(strip, Color(127,   0,   0))  # Red theater chase
		# colorWipe(strip, Color(  0,   0, 127))  # Blue theater chase
		# # Theater chase animations.
		# theaterChase(strip, Color(127, 127, 127))  # White theater chase
		# theaterChase(strip, Color(127,   0,   0))  # Red theater chase
		# theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
		# Rainbow animations.
		# rainbow(strip)
		# rainbowCycle(strip)
		# theaterChaseRainbow(strip)
