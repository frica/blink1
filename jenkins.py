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

INTERVAL = 30

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Check the status of a Jenkins job.')
    parser.add_argument('-u', '--url', help='url of the Jenkins job', required=True)
    args = parser.parse_args()

    url = args.url

    try:
        blink = Blink1()
    except RuntimeError:  # BlinkConnectionFailed(RuntimeError):
        print("No blink1 found, exiting now...")
        exit()

    iteration = 0

    try:
        while True:
            try:
                url += "/lastBuild/api/json"
                response = requests.get(url)
                response.raise_for_status()
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout, requests.exceptions.HTTPError):
                blink.fade_to_color(500, 'white')
                time.sleep(2)
                print("Unable to get the url, exiting now...")
                break

            try:
                jenkinsData = json.loads(response.text)
            except ValueError:
                print("Invalid json from ", url)
                break

            iteration += 1
            print("Check # ", iteration)
            if "result" in jenkinsData:
                print(jenkinsData["result"])
                if jenkinsData["result"] == "SUCCESS":
                    blink.fade_to_color(2000, "blue")
                    time.sleep(2)
                elif jenkinsData["result"] == "FAILURE":
                    blink.fade_to_color(2000, "red")
                    time.sleep(2)
            else:
                print("No result information in the json file.")
            time.sleep(INTERVAL)
            blink.fade_to_color(2000, "black")
            time.sleep(2)
    except KeyboardInterrupt:
        blink.fade_to_color(2000, "black")
    except Exception:
        blink.fade_to_color(2000, "black")
        raise

    blink.fade_to_color(2000, "black")
    blink.close()