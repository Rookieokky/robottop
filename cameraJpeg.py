#!/env/bin/python

import time
from SimpleCV import *
from SimpleCV.Display import Display

# initialize left Camera specification such as resolution and video frames
leftcamera = Camera(0, {"width": 1280, "height": 960})
js = JpegStreamer("http://192.168.2.6:8080")

while(1) 
		leftcamera.getImage().save(js)

# initialize right Camera specification such as resolution and video frames
rightcamera = Camera(1, {"width": 1280, "height": 960})
js = JpegStreamer("http://192.168.2.6:8090")

while(1) 
		rightcamera.getImage().save(js)

