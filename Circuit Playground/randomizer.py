from adafruit_circuitplayground import cp
import random
while True:
    if cp.acceleration.z < 0:
        for i in range(0,10):
            cp.pixels[i] = (random.randint(0,5),random.randint(0,5),random.randint(0,5))