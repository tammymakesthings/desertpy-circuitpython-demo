import time
import board
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
while True:
    pixel.fill((140, 25, 255))
    time.sleep(1.0)
    pixel.fill((0, 0, 0))
    time.sleep(1.0)
