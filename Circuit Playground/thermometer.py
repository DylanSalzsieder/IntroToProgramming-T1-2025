from adafruit_circuitplayground import cp
import time
while True:
    cp.pixels.fill((0,0,0))
    if cp.temperature*(9/5)+32 < 78:
        cp.pixels[0] = (0,0,1)
    if cp.temperature*(9/5)+32 > 78:
        cp.pixels[1] = (0,0,1)
    if cp.temperature*(9/5)+32 > 79:
        cp.pixels[2] = (0,0,1)
    if cp.temperature*(9/5)+32 > 80:
        cp.pixels[3] = (1,1,0)
    if cp.temperature*(9/5)+32 > 81:
        cp.pixels[4] = (1,1,0)
    if cp.temperature*(9/5)+32 > 82:
        cp.pixels[5] = (1,1,0)
    if cp.temperature*(9/5)+32 > 83:
        cp.pixels[6] = (1,1,0)
    if cp.temperature*(9/5)+32 > 84:
        cp.pixels[7] = (1,0,0)
    if cp.temperature*(9/5)+32 > 85:
        cp.pixels[8] = (1,0,0)
    if cp.temperature*(9/5)+32 > 86:
        cp.pixels[9] = (1,0,0)