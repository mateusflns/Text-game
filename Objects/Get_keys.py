import ctypes
from win32con import VK_UP, VK_DOWN, VK_LEFT, VK_RIGHT, VK_SPACE, VK_ESCAPE
import time
keys = 'QWERTYUIOP'

SCHARS = {'down' : VK_DOWN, 'up' : VK_UP, 'left' : VK_LEFT, 'right' : VK_RIGHT, 'space' : VK_SPACE, 'escape' : VK_ESCAPE}

def get_keys(key):
    if key in SCHARS:
        return ctypes.windll.user32.GetAsyncKeyState(SCHARS[key]) > 0
    return ctypes.windll.user32.GetAsyncKeyState(ord(key.upper())) > 0
