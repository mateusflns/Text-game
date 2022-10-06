from Engines.game_engine import Obj, Engine
from Engines.Get_keys import get_keys
from sys import exit
from random import randrange
from math import ceil

class Snake_engine(Engine):
    def run(self):
        
        # run all the objects and graphics
        self.graphic_engine.clear()
        xx = 0
        for obj in Engine.instances:

            obj.run()
            obj.update_bbox()
            if xx != 2:
                obj.draw_sprite()
            xx += 1
        self.graphic_engine.draw_map()

class Snake_Node(Obj):

    def run(self):
        self.time -= 1
        if self.time == 0: self.destroy(self)
        
        

class Fruit(Obj):
    def run(self):
  #      print("fruit Bbox",  self.bbox)
        pass


class Snake(Obj):


    def create(self):
        # direction = [x speed, y speed] (only one can be non zero)
        self.direction = [2,0]
        self.size = 5
        self.make_Fruit()
        

        self.x = Engine.tsize[0]/2
        self.y = int(Engine.tsize[1]/2)
        

    def run(self):
        
        
        #self.bbox = [self.bbox[0], self.bbox[1], self.bbox[2], self.bbox[3]]
        movex = get_keys('D') - get_keys('A')
        movey = get_keys('S') - get_keys('W')
     


        if movex and self.direction[0] == 0:
            self.direction = [movex*2, 0]
        elif movey and self.direction[1] == 0:
            self.direction = [0, movey]



        if self.colision_check(self.fruit.bbox)[0]:
            self.fruit.destroy(self.fruit)
            self.make_Fruit()   
            self.size +=1

        self.move(x=self.x + self.direction[0], y=self.y + self.direction[1])
        self.bbox[0] += movex
        self.bbox[2] += movex
        self.bbox[1] += movey
        self.bbox[3] += movey


        if self.colision_check(Snake_Node)[0]:
            pass#exit()
            
        a = Snake_Node(self.x, self.y, self.graphic_engine, sprite_path="./Snake/node.txt")
        a.time = self.size
        #xx = 0
                
        self.score = int(ceil(((self.size**2)*10)/100)) * 100
        self.graphic_engine.draw_text([1,1], f"Score: {self.score}")


        
    def make_Fruit(self):
        self.fruit = Fruit(0,0,self.graphic_engine, "./Snake/node.txt")
        while True:
            x = randrange(0, Engine.tsize[0])
            y = randrange(0, Engine.tsize[1])
            self.fruit.move(x=x, y=y)
            if not self.colision_check(self.fruit.bbox)[0]:
                break