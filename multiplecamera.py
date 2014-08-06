#!/Env/bin/python

from SimpleCV import *
import sys
import argparse


class leftEyesDisplay():

	_key = True
	_width = 640
	_height = 480

	def __init__(self,index,width = 640, height = 480):

			self.width = width
			self.height = height
			self.cam = Camera(index,prop_set={"width":self.width,"height":self.height})

	def setKey(self):
			if(self._key):
					self._key = False

			else:
					self._key = True

	def getVideo(self):
			video = self.cam.getImage()
			if(self._key):
						return video
			else:
						return "error"

#Make two camera objects 
leftCamera = Camera(0)
rightCamera = Camera(1)
width = leftCamera.width+rightCamera.width
displ = Display((width,cam1.height),0,'SimpleCV tutorial')

print("\n >>>Right click on the Image to exit!")

while disp.isNotDone():
	img1 = leftCamera.getNewImage()
	img2 = rightCamera.getNewImage()
	img3 = img1.sideBySide(img2)

	dwn = disp.leftButtonDownPosition()
	if (dwn is not None and dwn[0] <640):
		cam1.setKey()
	elif (dwn is not None and dwn[0] >= 640):
		cam2.setKey()

	img3.drawText("Camera 1",100,400,fontsize=40,color=Color.BLUE)
	img3.drawText("Camera 2",840,400,fontsize=40,color=Color.GREEN)
	img3.save(disp)
	if disp.mouseRight:
		break
print("\n >>>Program Exitted")
