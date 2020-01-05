import time
from adafruit_hid.mouse import Mouse
import board
import adafruit_dotstar as dotstar
import random

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

mouse = Mouse()

while True:
    dot[0]=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
    mouse.move(x=64,y=64)
    time.sleep(1)
    mouse.move(x=-64,y=64)
    time.sleep(1)
    mouse.move(x=-64,y=-64)
    time.sleep(1)
    mouse.move(x=64, y=-64)
    time.sleep(1)

