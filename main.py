import time
import os
from graphics import *
from objects import *
from random import randrange


os.system('cls')
os.system('mode con:cols=160 lines=60')

tsize = os.get_terminal_size()
tsize = [tsize.columns, tsize.lines]
map = Char_map(tsize[0], tsize[1])
hsp = 1
vsp = 1
coords = [tsize[0]/2, tsize[1]/2]
engine = Engine(map)
p1 = Player(int(coords[0]), int(coords[1]), 'sprite_exemple.txt', map)
p2 = Dummy(int(coords[0]) + 12, int(coords[1]), 'sprite_exemple.txt', map)

for i in range(100):
    time.sleep(0.3)
    p1.x += hsp
    engine.run()
