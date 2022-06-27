from Engines.game_engine import Obj, Engine
from Engines.Get_keys import get_keys


class Snake_Node(Obj):


    def run(self):
        if self.time <= 0: self.destroy(self.id)
        self.time -= 1
        


class Snake(Obj):


    def create(self):
        # direction = [x speed, y speed] (only one can non zero)
        self.direction = [1,0]
        self.size = 4

    def run(self):
        self.move(x=self.x + self.direction[0], y=self.y + self.direction[1])
    
        movex = get_keys('D') - get_keys('A')
        movey = get_keys('S') - get_keys('W')
        if movex:
            self.direction = [movex, 0]
        elif movey:
            self.direction = [0, movey]

        a = Snake_Node(self.x, self.y, self.graphic_engine, sprite_path="./Snake/node.txt")
        a.time = self.size