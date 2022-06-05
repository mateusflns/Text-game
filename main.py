import time
import os
from graphics import *
from random import randrange

os.system('cls')
os.system('mode con:cols=160 lines=60')
import time

tsize = os.get_terminal_size()
tsize = [tsize.columns, tsize.lines]
map = Char_map(tsize[0], tsize[1])
hsp = 1
vsp = 1
coords = [tsize[0]/2, tsize[1]/2]

map.clear()
map.draw_line([8,10],[10,20])

map.draw_map()