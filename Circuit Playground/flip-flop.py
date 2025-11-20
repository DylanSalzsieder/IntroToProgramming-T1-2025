from adafruit_circuitplayground import cp
import time
while True:
    cp.pixels.fill((0,0,0))
    if cp.switch:
        cp.pixels[0] = (0,5,0)
        cp.pixels[1] = (0,5,0)
        cp.pixels[2] = (0,5,0)
        cp.pixels[3] = (0,5,0)
        cp.pixels[4] = (0,5,0)
    else:
        cp.pixels[5] = (0,5,0)
        cp.pixels[6] = (0,5,0)
        cp.pixels[7] = (0,5,0)
        cp.pixels[8] = (0,5,0)
        cp.pixels[9] = (0,5,0)