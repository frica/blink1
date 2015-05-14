#!/usr/bin/env python

""" Find matches in clipboard text

"""

import time
from blink1.blink1 import Blink1
import pyperclip
import re

if __name__ == '__main__':

    text = str(pyperclip.paste())
    matches = []

    matches = re.findall(r"frica[\w]*", text)
    print("# of matches:", len(matches))

    # Using it without context manager will leave the blink(1) at the end of execution.
    b1 = Blink1()

    # Blink as many times as it found the text
    if len(matches) > 0:
        print(matches)
        for i in enumerate(matches, start=1):
            print("blink #", i)
            # red (no kidding)
            b1.fade_to_color(500, 'red')
            time.sleep(1)
            # black
            b1.fade_to_rgb(1000, 0, 0, 0)
            time.sleep(1)