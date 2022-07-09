import time
from random import randint
import board
import terminalio
from adafruit_display_text import label

display = board.DISPLAY

text = "HELLO WORLD"
font = terminalio.FONT
color = 0x0000FF

text_area = label.Label(font, text=text, color=color)
text_area.x = 100
text_area.y = 80
display.show(text_area)

while True:
    time.sleep(0.5)
    text_area.x = random.randint(1, 120)
    text_area.y = random.randint(1, 120)
