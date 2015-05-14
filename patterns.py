#!/usr/bin/env python

""" Load blinking patterns defined in BlinkControl

"""
import json
import time
from blink1.blink1 import Blink1


def hex_to_rgb(value):
    """ Useful convert method from http://stackoverflow.com/a/214657 """
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def play_simple_pattern(pattern, blink):
    """ play a simple pattern with 2 colors
    Example: ['3', '#ff00ff', '0.5', '0', '#000000', '0.5', '']
    """
    repeat = int(pattern[0])
    first_color = pattern[1]
    fade_first_color = float(pattern[2])
    fade_first_color = int(fade_first_color * 1000)
    print(fade_first_color)
    led_fc = pattern[3]
    sec_color = pattern[4]
    fade_sec_color = int(float(pattern[5]) * 1000)
    led_sc = pattern[6]
    print("We will flash {0} times between {1} and {2}".format(repeat, first_color, sec_color))
    for idx in range(0, repeat):
        blink.fade_to_rgb(fade_first_color, hex_to_rgb(first_color)[0], hex_to_rgb(first_color)[1],
                          hex_to_rgb(first_color)[2])
        time.sleep(1)
        blink.fade_to_rgb(fade_sec_color, hex_to_rgb(sec_color)[0], hex_to_rgb(sec_color)[1], hex_to_rgb(sec_color)[2])
        time.sleep(1)


blink = Blink1()

try:
    patternFile = open('patternsReadOnly.json', 'r')
    patternData = json.load(patternFile)
except ValueError:
    print("Invalid json from ", patternFile)
    exit()

# pretty print json data
# print(json.dumps(patternData, indent=1))

print("# of patterns found: {}".format(len(patternData)))

if len(patternData) != 0:
    for i in range(0, len(patternData)):
        pattern = [x.strip() for x in patternData[i]["pattern"].split(',')]
        print("Pattern: {}".format(patternData[i]["name"]))
        if i < 6:
            print("Simple pattern detected, let's play it!")
            play_simple_pattern(pattern, blink)

blink.fade_to_rgb(1000, 0, 0, 0)
blink.close()

patternFile.close()