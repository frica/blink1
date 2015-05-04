import time
from blink1.blink1 import blink1

with blink1() as b1:
    b1.fade_to_color(100, 'navy')
    time.sleep(2)
    b1.fade_to_color(1000, 'white', 0) # Set both to white
    b1.fade_to_color(1000, 'red', 1) # Set LED 1 to red
    b1.fade_to_color(1000, 'green', 2) # Set LED 2 to green
    time.sleep(10)

