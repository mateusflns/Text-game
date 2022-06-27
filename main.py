import time
import os
from Engines.graphic import *
from Engines.game_engine import Engine
from random import randrange
from simple_functions import *
from Snake.Snake import Snake, Snake_Node

os.system('cls')
maximize()

tsize = os.get_terminal_size()
tsize = [tsize.columns, tsize.lines]
map = Char_map(tsize[0], tsize[1])
coords = [tsize[0]/2, tsize[1]/2]
engine = Engine(map,tsize)
p1 = Snake(0, 0, map, "./Snake/head.txt")

fps = 7
delay = 1/fps
while True:
    stime = time.time() 
    engine.run()
    if time.time() - stime < delay:
        time.sleep(abs(delay - (time.time() - stime)))