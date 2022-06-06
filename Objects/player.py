from Objects.objects import Obj, Dummy, Wall, Engine
from Objects.Get_keys import get_keys
from math import copysign

class Player(Obj):
    def __init__(self, x, y, graphic_engine, sprite_path = '', bbox = []):
        Obj.__init__(self, x, y, graphic_engine, sprite_path, bbox)


    def run(self):
        if get_keys('D'):
            move = 1
        elif get_keys('A'):
            move = -1
        else: move = 0
        self.hsp = move * self.spd

        if self.vsp < self.max_grv:
            self.vsp += self.grv

        if get_keys('space'):
            self.vsp = self.jspd


        if self.wall_check('x'):
            self.hsp = copysign(1, self.hsp)
            while not self.wall_check('x'):
                self.x += self.hsp
            self.hsp = 0

        if self.wall_check('y'):
            self.vsp = 0

        self.x += self.hsp
        self.y += int(self.vsp)


    def create(self):
        self.hsp = 0
        self.vsp = 0
        self.grv = 0.3
        self.max_grv = 3
        self.spd = 5
        self.jspd = -3


    def wall_check(self, c):
        if c == 'x':
            for i in Engine.instances:
                if isinstance(i, Wall):
                    if self.colision_check(i.bbox, [self.bbox[0] + self.hsp, self.bbox[1],self.bbox[2] + self.hsp, self.bbox[3]]):
                        return True
            return False
        else:
            for i in Engine.instances:
                if isinstance(i, Wall):
                    #print(self.colision_check(i.bbox, [self.bbox[0], self.bbox[1] + int(self.vsp),self.bbox[2], self.bbox[3] + (self.vsp)]))
                    if self.colision_check(i.bbox, [self.bbox[0], self.bbox[1] + int(self.vsp),self.bbox[2], self.bbox[3] + int(self.vsp)]):
                        return True
            return False