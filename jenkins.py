#!/usr/bin/env python

""" Detect if a Jenkins build is successful or not

Example usage (on Ubuntu):

python3 jenkins.py -u=https://builds.apache.org/job/AuroraBot

"""

from blink1.blink1 import Blink1
import requests
import time
import json
import argparse

parser = argparse.ArgumentParser(description='Check the status of a Jenkins job.')
parser.add_argument('-u', '--url', help='url of the Jenkins job', required=True)
args = parser.parse_args()

url = args.url

try:
    blink = Blink1()
except RuntimeError:  # BlinkConnectionFailed(RuntimeError):
    print("No blink1 found, exiting now...")
    exit()

try:
    response = requests.get(url + "/lastBuild/api/json")
    response.raise_for_status()
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    blink.fade_to_color(500, 'white')
    time.sleep(2)
    print("Unable to get the url, exiting now...")
    exit()

try:
    jenkinsData = json.loads(response.text)
except ValueError:
    print("invalid json")
else:
    if "result" in jenkinsData:
        print(jenkinsData["result"])
        if jenkinsData["result"] == "SUCCESS":
            blink.fade_to_color(2000, "blue")
            time.sleep(2)
        elif jenkinsData["result"] == "FAILURE":
            blink.fade_to_color(2000, "red")
            time.sleep(2)

blink.fade_to_rgb(1000, 0, 0, 0)
blink.close()