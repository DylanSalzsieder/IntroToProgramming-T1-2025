from adafruit_circuitplayground import cp
import random
while True:
    if cp.button_a:
        cp.pixels.fill((0,0,0))
        x = random.randint(0,10)
        for i in range(0,x):
            cp.pixels[i] = (5,0,0)
    elif cp.button_b:
        cp.pixels.fill((0,0,0))