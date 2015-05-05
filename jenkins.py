#!/usr/bin/env python

from blink1.blink1 import Blink1
import requests
import time

blink = Blink1()

url = "https://jenkins.qa.ubuntu.com/api/python"

try:
    resp = requests.get(url, timeout=30).text
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    blink.fade_to_color(500, 'white')

print(resp)
