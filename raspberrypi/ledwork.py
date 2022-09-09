from rpi_ws281x import * 
import time

LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT,LED_PIN,LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

m = 0
while m < 20:
  for x in range(0, LED_COUNT):
    strip.setPixelColor(x, Color(0))
  strip.show()
  for x in range(0, LED_COUNT):
    strip.setPixelColor(x + 1, Color(255,1,1))
    strip.show()
    strip.setPixelColor(x + 2, Color(1,1,255))
    strip.show()
    strip.setPixelColor(x + 3, Color(1,255,1))
    strip.show()
    time.sleep(.1)
    for x in range(0, LED_COUNT):
      strip.setPixelColor(x, Color(0))
    strip.show()
  m = m+1