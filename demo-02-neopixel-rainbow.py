import time
import board
from rainbowio import colorwheel
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=False)
while True:
    for i in range(255):
        pixels.fill(colorwheel(i % 255))
        pixels.show()
        time.sleep(0.1)
