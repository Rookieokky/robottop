#!/ENV/bin/python

import time
from SimpleCV import *

# initialize left Camera specification such as resolution and video frames
leftcamera = Camera(0, {"width": 1280, "height": 960})
# initialize right Camera specification such as resolution and video frames
rightcamera = Camera(1, {"width": 1280, "height": 960})

leftcamera.getImage().save("left.jpg")
rightcamera.getImage().save("right.jpg")

