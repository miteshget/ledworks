import time
import random

LED_COUNT      = 120  

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

def flare1():
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
            # strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
            # leds[int(sparkPos[i])] = HeatColor(sparkCol[i])
            # leds[int(sparkPos[i])] %= 50; 

        strip.setPixelColor(round(flarePos), Color(0,0,round(brightness * 255))
        strip.show()
        clean(strip)
        flarePos += flareVel
        flareVel += gravity
        brightness *= .99
flare1()


  

  FastLED.clear(); while (flareVel >= -.05) {
    for (int i = 0; i < 5; i++) {
      sparkPos[i] += sparkVel[i];
      sparkPos[i] = constrain(sparkPos[i], 0, 120);
      sparkVel[i] += gravity;
      sparkCol[i] += -.8;
      sparkCol[i] = constrain(sparkCol[i], 0, 255);
      leds[int(sparkPos[i])] = HeatColor(sparkCol[i]);
      leds[int(sparkPos[i])] %= 50; 
    }
   leds[int(flarePos)] = CHSV(0, 0, int(brightness * 255));
   FastLED.show();
   FastLED.clear();
   flarePos += flareVel;
   flareVel += gravity;
   brightness *= .99;
  }
}