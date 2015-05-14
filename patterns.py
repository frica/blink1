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


def play_pattern(pattern, blink):
    """ play a pattern with multiple colors
    Example: ['6', '#ff0000', '0.3', '1', '#0000ff', '0.3', '2', '#000000', '0.1', '0', '#ff0000', '0.3', '2', '#0000ff', '0.3', '1', '#000000', '0.1', '0']
    """
    print(pattern)
    repeat = int(pattern[0])

    print("We will repeat {0} times this pattern.".format(repeat))
    for loop in range(0, repeat):
        index = 1
        for i in range(0, len(pattern) // 3):
            fade = int(float(pattern[index + 1]) * 1000)
            led = int(pattern[index + 2]) if pattern[index + 2] else 0
            if loop == 0:
                print("Color {0} (Index {1}): {2} - LED {3} - Fade {4}".format(i+1, index, pattern[index], led, fade))
            blink.fade_to_rgb(fade, hex_to_rgb(pattern[index])[0], hex_to_rgb(pattern[index])[1],
                              hex_to_rgb(pattern[index])[2], led)
            time.sleep(1)
            index += 3

if __name__ == '__main__':

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
            play_pattern(pattern, blink)

    blink.fade_to_rgb(1000, 0, 0, 0)
    blink.close()

    patternFile.close()