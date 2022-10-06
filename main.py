import time
import os
from Engines.graphic import *
from Engines.game_engine import Engine
from Engines.Get_keys import get_keys
from random import randrange
from simple_functions import maximize
from Snake.Snake import Snake, Snake_Node, Snake_engine


os.system('cls')
maximize()


tsize = os.get_terminal_size()
tsize = [tsize.columns, tsize.lines]
map = Char_map(tsize[0], tsize[1])
fps = 18
delay = 6/fps
engine = Snake_engine(map,tsize)


coords = [tsize[0]/2, tsize[1]/2]
p1 = Snake(0, 0, map, "./Snake/head.txt")


while True:

    Snake_engine.running = True
    engine.run()

    stime = time.time() 

    delay = 1/p1.size

    if time.time() - stime < delay:
        time.sleep(abs(delay - (time.time() - stime)))