from adafruit_circuitplayground import cp
import time
while True:
    cp.pixels.fill((0,0,0))
    if cp.light < 30:
        cp.pixels[0] = (5,5,5)
    if cp.light < 27:
        cp.pixels[1] = (5,5,5)
    if cp.light < 24:
        cp.pixels[2] = (5,5,5)
    if cp.light < 21:
        cp.pixels[3] = (5,5,5)
    if cp.light < 18:
        cp.pixels[4] = (5,5,5)
    if cp.light < 15:
        cp.pixels[5] = (5,5,5)
    if cp.light < 12:
        cp.pixels[6] = (5,5,5)
    if cp.light < 9:
        cp.pixels[7] = (5,5,5)
    if cp.light < 6:
        cp.pixels[8] = (5,5,5)
    if cp.light < 3:
        cp.pixels[9] = (5,5,5)