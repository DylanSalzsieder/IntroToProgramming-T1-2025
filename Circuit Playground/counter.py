from adafruit_circuitplayground import cp
import time
x = 0
while True:
    if cp.button_a and x<10:
        cp.pixels.fill((0,0,0))
        x += 1
        for i in range(0,x):
            cp.pixels[i] = (5,0,0)
        time.sleep(0.3)
    elif cp.button_b and x>0:
        cp.pixels.fill((0,0,0))
        x -= 1
        for i in range(0,x):
            cp.pixels[i] = (5,0,0)
        time.sleep(0.3)