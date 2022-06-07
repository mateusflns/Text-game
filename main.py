import time
import os
from graphics import *
from Objects import player, objects
from random import randrange
from simple_functions import *

os.system('cls')
maximize()

tsize = os.get_terminal_size()
tsize = [tsize.columns, tsize.lines]
map = Char_map(tsize[0], tsize[1])
coords = [tsize[0]/2, tsize[1]/2]
engine = objects.Engine(map,tsize)
p1 = player.Player(int(coords[0]), int(coords[1]), map, 'sprite_exemple.txt')


while True:
    time.sleep(0.1)
    engine.run()
