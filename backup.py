import sys
import platform
import usb.core
import usb.util
import cv2
import numpy as np


def enterToExit():
    print()
    input("Press Enter to Exit...")
    sys.exit(0)


dev = usb.core.find(idVendor=1452, idProduct=4776)

if dev == None:
    print("iOS device not found.")
    enterToExit()

path = usb.util.get_string(dev, dev.iProduct)
vid = dev.idVendor
pid = dev.idProduct
print(path, vid, pid)


plat = platform.system()
if plat == "Windows":
    path = ""
elif plat == "Darwin":
    path = ""
else:
    print("Platform not supported")
    enterToExit()