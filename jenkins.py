#!/usr/bin/env python

from blink1.blink1 import Blink1
import requests
import time
import json

blink = Blink1()

# example job
url = 'https://builds.apache.org/job/AuroraBot/lastBuild/api/json'

try:
    response = requests.get(url)
    response.raise_for_status()
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    blink.fade_to_color(500, 'white')

try:
    jenkinsData = json.loads(response.text)
except ValueError:
    print("invalid json")
else:
    print(jenkinsData)
    if "result" in jenkinsData:
        print(jenkinsData["result"])
        if jenkinsData["result"] == "SUCCESS":
            blink.fade_to_color(2000, "blue")
            time.sleep(2)

blink.fade_to_rgb(1000, 0, 0, 0)
blink.close()