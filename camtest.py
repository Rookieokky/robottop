#!/Env/bin/python

from SimpleCV.base import *
import sys
import argparse
import webbrowser
import cv2
from SimpleCV import Shell
import sys

if len(sys.argv) > 1:
		Shell.main(sys.argv)
else: 
		Shell.main()

# initialize left camera
class LeftEyedisplay():

	leftcamera = Camera(0,{"width": 1280, "height": 960})	
	vs = VideoStream(leftcamera, 25, true)
	display = Display()
	leftcamera.getImage().save(vs)

# initialize right camera 
class RightEyedisplay():
	
	rightcamera = Camera(1,{"width": 1280, "height": 960})
	vs = VideoStream(rightcamera, 25, true)
	display = Display()
	rightcamera.getImage().save(vs)


