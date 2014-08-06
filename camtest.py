#!/Env/bin/python

from SimpleCV.base import *
import sys
import argparse


# initialize left camera class
class LeftEyedisplay():


	# this function defines the left camera specs
	def leftcamera(self):
			lefteye = Camera(0, {"width": 1280, "height": 960})
			lefteye.live()


# initialize right camera class
class RightEyedisplay():
	
	def rightcamera(self):
			righteye = Camera(1, {"width": 1280, "height":960})
			righteye.live()


