#!/ENV/bin/python
import time 
from SimpleCV import*

vs = VideoStream("/dev/video0","/dev/video1", "./output_http.so","./input_uvc.so", fps=20)
vs.live()
