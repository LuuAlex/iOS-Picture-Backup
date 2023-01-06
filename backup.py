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


dev = usb.core.find(idVendor=1452, idProduct=4776) #ID For iPhones

if dev == None:
    print("iOS device not found.")
    enterToExit()

for cfg in dev:
    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')

path = usb.util.get_string(dev, dev.id)
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