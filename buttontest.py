#!/env/bin/python

import time
from Tkinter import *
import serial

def quit():
	global Tktop
	Tktop.destroy()

def FORWARD():
	ser.write('f')

def BACKWARD():
	ser.write('b')

def RIGHT():
	ser.write('r')

def LEFT():
	ser.write('l')

def STOP():
	ser.write('s')

ser = serial.Serial('/dev/ttyACM0', 9600)
print("Connecting to Arduino")
time.sleep(3)

GUI = Tk()
GUI.geometry("210x90")
GUI.title("CEFA controller")
B1 = Button(text="FORWARD", command = FORWARD)
B1.grid(row=0, column=1)

B2 = Button(text="LEFT", command = LEFT)
B2.grid(row=0, column=0,)

B3 = Button(text="STOP", command = STOP)
B3.grid(row=1, column=1,)

B4 = Button(text="RIGHT", command = RIGHT)
B4.grid(row=1, column=2 )

B5 = Button(text="BACKWARD", command = BACKWARD)
B5.grid(row=2, column=1)

mainloop()

