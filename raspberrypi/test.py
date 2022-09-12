import time
import random

LED_COUNT      = 120  

sparkPos = []
sparkVel = []
sparkCol = []
gravity = -.0019

for i in range(0, 7):
    sparkPos.insert(i, '')
    sparkVel.insert(i, '')
    sparkCol.insert(i, '')


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


def flare1(c):
    flarePos = 0
    flareVel = float(random.getrandbits(16)) / 90
	# flareVel = float(random16(60, 80)) / 90
    brightness = float(1)
    for i in range(0,5,1):
        # print(flarePos)
        # print(flareVel)
        # print(brightness)
        sparkPos[i] = 0
        sparkVel[i] = (float(random.getrandbits(8) / 255) * (flareVel / 5))
        sparkCol[i] = sparkVel[i] * 1000
        sparkCol[i] = constrain(sparkCol[i], 0, 255)
        # print(flarePos)
        # print(flareVel)
        # print(brightness)
        # print(sparkPos)
        # print(sparkVel)
        # print(sparkCol)
    while flareVel >= -.05:
        for i in range(0,5,1):
            sparkPos[i] += sparkVel[i]
            sparkPos[i] = constrain(sparkPos[i], 0, 120)
            sparkVel[i] += gravity
            sparkCol[i] += -.8
            sparkCol[i] = constrain(sparkCol[i], 0, 255)
            # strip.setPixelColor(i-s,Color(round(a*pow(.7,s)),round(b*pow(.7,s)),round(c*pow(.7,s))))
            # leds[int(sparkPos[i])] = HeatColor(sparkCol[i])
            sparkPos[i] %= 50
            print(round(sparkCol[i]))
            print(round(sparkPos[i]))
            c += 1
            print(str(c) + ' ----------')
        # break
        flarePos += flareVel
        flareVel += gravity
        brightness *= .99
c = 0
flare1(c)

