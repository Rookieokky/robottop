#!/env/bin/python

import serial
import glob

def scan():
    """scan for available ports. return a list of device names."""
    return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')

if __name__=='__main__':
    print "Found ports:"
    for name in scan():
        print name
