from ctypes import windll, Structure, c_long, byref
import time


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

try:
	while True:

		pos = queryMousePosition()
		print(pos)
		time.sleep(1)
except KeyboardInterrupt:
    pass