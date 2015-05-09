# blink1 playground

My scripts using blink(1) USB RGB LED by ThingM http://blink1.thingm.com/

*Inspired from examples in https://github.com/todbot/blink1/tree/master/python/pypi*

# Use

Simply run like this:

	python3 demo1.py

**Note**

* demo1.py needs you to compile from source the latest version of the python API, at least if you are using Ubuntu. 
* jenkins.py is inspired by https://github.com/msherry/blink-jenkins

**Note about BlinkControl**

The tool also works on linux.

First do:

	sudo apt-get install libusb-1.0-0-dev

Go to the folder commandline and 

	make

Then install:

	sudo apt-get install libgl1-mesa-dev
	sudo apt-get install mesa-common-dev

Install qt5.3 (you'll need to create an account http://www.qt.io/download-open-source/)

Start QTCreator and open qt/blink1control/blink1control.pro
Click Rebuild: here it is!

