from Objects.objects import Obj, Wall, Engine
from Objects.Get_keys import get_keys
from math import copysign

class Player(Obj):
    def __init__(self, x, y, graphic_engine, sprite_path = '', bbox = []):
        Obj.__init__(self, x, y, graphic_engine, sprite_path, bbox)


    def run(self):
        # move is 1 or -1 depending on the direction or 0 if not moving
        move = get_keys('D') - get_keys('A')
        self.hsp = move * self.spd

        # add gravity to vsp if not at max grv
        if self.vsp < self.max_grv:
            self.vsp += self.grv

        if get_keys('space') and self.colision_check(Wall, [self.bbox[0], self.bbox[3], self.bbox[2], self.bbox[3]+1])[0]:
            self.vsp = self.jspd
        
        self.y_colision()
        self.x_colision()

        # change x and y according to hsp and vsp
        self.move(x = self.x + self.hsp,
        y = self.y + int(self.vsp))
        


    def create(self):
        self.hsp = 0
        self.vsp = 0
        self.grv = 0.3
        self.max_grv = 3
        self.spd = 5
        self.jspd = -3


    def x_colision(self):
        # x and y colision could be combined into one function 
        # but they are separated for better readability
        if self.hsp:
            hsp_sign = copysign(1, self.hsp)

            if self.hsp > 0:

                if self.colision_check(Wall, [self.bbox[2],
                self.bbox[1], self.bbox[2] + self.hsp, self.bbox[3]])[0]:

                    while not self.colision_check(Wall, [self.bbox[2],
                    self.bbox[1], self.bbox[2] + hsp_sign, self.bbox[3]])[0]:

                        self.move(x = self.x + hsp_sign)
                        
                    self.hsp = 0

            else:

                if (self.colision_check(Wall, [self.bbox[0] + self.hsp,
                self.bbox[1], self.bbox[0] , self.bbox[3]])[0]): 

                    while not self.colision_check(Wall, [self.bbox[0] + hsp_sign,
                    self.bbox[1], self.bbox[0], self.bbox[3]])[0]:

                        self.move(x = self.x + hsp_sign)
                        
                    self.hsp = 0


    def y_colision(self):
        if self.vsp:
            if self.vsp > 0:
                dir = [0,3,2,3]
            else:
                dir = [0,1,2,1] 

            vsp_sign = copysign(1, self.vsp)

            if self.colision_check(Wall, [self.bbox[dir[0]] ,
            self.bbox[dir[1]] + -vsp_sign, self.bbox[dir[2]], self.bbox[dir[3]] + int(self.vsp)+vsp_sign])[0]:

                while not self.colision_check(Wall, [self.bbox[dir[0]] ,
                self.bbox[dir[1]], self.bbox[dir[2]], self.bbox[dir[3]] + vsp_sign])[0]:

                    self.move(y = self.y + vsp_sign)
                self.vsp = 0 