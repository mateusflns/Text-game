from Engines.game_engine import Obj, Engine
from Engines.Get_keys import get_keys
from os import system
from random import randrange


class Snake_Node(Obj):


    def run(self):
        if self.time <= 0: self.destroy(self)
        self.time -= 1
        

class Fruit(Obj):
    pass


class Snake(Obj):


    def create(self):
        # direction = [x speed, y speed] (only one can non zero)
        self.direction = [1,0]
        self.size = 4

        self.make_Fruit()


    def run(self):
        self.move(x=self.x + self.direction[0], y=self.y + self.direction[1])
    
        movex = get_keys('D') - get_keys('A')
        movey = get_keys('S') - get_keys('W')
        
        a = Snake_Node(self.x, self.y, self.graphic_engine, sprite_path="./Snake/node.txt")

        if movex and self.direction[0] == 0:
            self.direction = [movex, 0]
        elif movey and self.direction[1] == 0:
            self.direction = [0, movey]

        a.time = self.size
        if self.colision_check(self.fruit.bbox)[0]:
            self.fruit.destroy(self.fruit)
            self.make_Fruit()
            self.size +=1
        
        if self.colision_check(Snake_Node)[0]:
            system("exit")

        
    def make_Fruit(self):
        self.fruit = Fruit(0,0,self.graphic_engine, "./Snake/node.txt")
        while True:
            x = randrange(0, Engine.tsize[0])
            y = randrange(0, Engine.tsize[1])
            self.fruit.move(x=x, y=y)
            if not self.colision_check(self.fruit.bbox)[0]:
                break