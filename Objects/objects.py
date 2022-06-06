class Obj:
    def __init__(self, x, y, graphic_engine, sprite_path = '', bbox = []):
        if sprite_path:
            self.sprite_path = sprite_path
            self.load_sprite()
        else:
            self.sprite = ''

        self.load_coords(x, y, bbox)
        self.graphic_engine = graphic_engine
        Engine.instances.append(self)
        self.id = Engine.instances.index(self)
        self.create()


    def load_coords(self, x, y, bbox = []):
        self.x = x
        self.y = y
        self.x2 = x + len(self.sprite[0])
        self.y2 = y + len(self.sprite)
        self.sbbox = False
        if not bbox:
            self.bbox = [x, y, self.x2, self.y2]
        else:
            self.sbbox = True
            self.bbox = bbox


    def update_bbox(self):
        if not self.sbbox:
            self.x2 = self.x + len(self.sprite[0])
            self.y2 = self.y + len(self.sprite)
            self.bbox = [self.x, self.y, self.x2, self.y2]


    def load_sprite(self):
        file = open(self.sprite_path, 'r')
        sprite = file.readlines()
        file.close()
        nsprite = []
        for line in sprite:
            nsprite.append(line.strip('\n'))
        self.sprite = nsprite


    def colision_check(self, bbox2, bbox1 = []):
        # if bbox2 is a object check colision with all the instances of that object
        if not type(bbox2) == list:
            # loop through all objects
            for i in Engine.instances:
                # check if the object is the same as given          check if the object isn't itself

                if i.__class__.__name__ == str(bbox2)[16:].split("'>")[0] and i != self:
                    #check for colision
                    
                    if self.colision_check(i.bbox, bbox1):
                        return i.id
            return False
        
        if not bbox1:
            bbox1 = self.bbox


        b1width = bbox1[2] - bbox1[0]
        b1height = bbox1[3] - bbox1[1]
        b2width = bbox2[2] - bbox2[0]
        b2height = bbox2[3] - bbox2[1]

        if (bbox1[0] < bbox2[0] + b2width and
            bbox1[0] + b1width > bbox2[0] and
            bbox1[1] < bbox2[1] + b2height and
            bbox1[1] + b1height > bbox2[1]):
                return True

        return False


    def draw_sprite(self):
        if self.sprite:
            self.graphic_engine.draw_sprite([self.x, self.y], self.sprite)


    def run(self):
        pass


    def create(self):
        pass

    
    def destroy(self, id):
        '''Unfortunaly you can't delete an object from a list in python,
        removing it from the list will stop it from being drawn and run'''
        Engine.instances.pop(id)



class Engine():
    def __init__(self, graphic_engine, tsize, background_sprite = ''):
        Engine.instances = []
        self.tsize = tsize
        self.graphic_engine = graphic_engine
        if background_sprite:
            self.background_sprite = graphic_engine.load_sprite(background_sprite)


    def run(self):
        self.graphic_engine.clear()
        self.graphic_engine.draw_rectangle([0,self.tsize[1]-8],[self.tsize[0],self.tsize[1]], '#')
        for obj in Engine.instances:
            obj.run()
            obj.update_bbox()
            obj.draw_sprite()
        self.graphic_engine.draw_map()

    

    def draw_background(self):
        if self.background_sprite:
            self.graphic_engine.draw_sprite([0, 0], self.background_sprite)



class Dummy(Obj):
    def __init__(self, x, y, graphic_engine, sprite_path = '', bbox = []):
        Obj.__init__(self, x, y, graphic_engine, sprite_path, bbox)



class Wall():
    '''
    Wall object for colision checking no sprite is drawn
    '''
    def __init__(self,bbox = []):
        '''
        Only bbox needed since wall is only for colision
        '''
        Engine.instances.append(self)
        self.id = Engine.instances.index(self)
        self.bbox = bbox

    def run(self):
        pass

    def update_bbox(self):
        pass

    def draw_sprite(self):
        pass