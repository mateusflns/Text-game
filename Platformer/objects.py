MAPS = []
def make_maps(tsize):
    global MAPS
    # colision maps with bbox for drawing and making walls
    MAPS.append([[[69, tsize[1]-12], [71, tsize[1]-10]],
                 [[1, tsize[1]-4], [tsize[0]-1, tsize[1]-1]],
                 [[22, tsize[1]-15], [32, tsize[1]-13]],
                 [[33, tsize[1]-12], [44, tsize[1]-10]],
                 [[45, tsize[1]-11], [53, tsize[1]-9]],
                 [[62, tsize[1]-12], [64, tsize[1]-10]],
                 [[14, tsize[1]-8], [17, tsize[1]-5]]])



class Obj:
    '''
    Base object to be inherited from
    '''

    def __init__(self, x : int, y : int, graphic_engine, sprite_path = '', bbox = []):

        # basic variable assignment 
        self.sprite_path = sprite_path
        self.load_sprite()
        
        self.load_coords(x, y, bbox)

        self.graphic_engine = graphic_engine
        Engine.instances.append(self)
        self.id = Engine.instances.index(self)

        # create code for running once when the object is created 
        # inherited classes can override this
        self.create()


    def load_coords(self, x, y, bbox = []):
        
        # loading coords and bounding box 
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
        
        # update the bounding box
        if not self.sbbox:

            self.x2 = self.x + len(self.sprite[0])
            self.y2 = self.y + len(self.sprite)
            self.bbox = [self.x, self.y, self.x2, self.y2]


    def load_sprite(self):
        
        # load the sprite from the sprite path
        file = open(self.sprite_path, 'r')
        sprite = file.readlines()
        file.close()

        # convert the sprite to a list of strings
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
                objname = str(i).split(' ')[0].split('.')[2]

                if i.__class__.__name__ == objname and i != self:
                    
                    #check for colision     
                    if self.colision_check(i.bbox, bbox1)[0]:
                        return [True, i.id]
            
            return [False, None]

        # if bbox 1 is not given use the object's bbox
        if not bbox1:
            bbox1 = self.bbox


        # calculate width and height of the bounding boxes
        b1width = bbox1[2] - bbox1[0]
        b1height = bbox1[3] - bbox1[1]
        b2width = bbox2[2] - bbox2[0]
        b2height = bbox2[3] - bbox2[1]

        # check if the bounding boxes are overlapping
        if (bbox1[0] < bbox2[0] + b2width and
            bbox1[0] + b1width > bbox2[0] and
            bbox1[1] < bbox2[1] + b2height and
            bbox1[1] + b1height > bbox2[1]):
            return [True, None]

        return [False, None]


    def draw_sprite(self):
        if self.sprite:
            self.graphic_engine.draw_sprite([int(self.x), int(self.y)], self.sprite)


    def run(self):
        pass


    def create(self):
        pass

    
    def destroy(self, id):
        '''
        Destroy the object
        '''
        Engine.instances.pop(id)


    def move(self, x = False, y = False) -> None:
        '''
        Move method for auto updating bbox
        '''
        if x: self.x = x
        if y: self.y = y
        self.update_bbox()


class Engine():
    '''
    Engine for haldling the objects and updating them
    '''
    def __init__(self, graphic_engine, tsize, background_sprite = ''):
        
        # list of all the objects that should be drawn and 
        Engine.instances = []
        self.graphic_engine = graphic_engine
    
        # size of screen and map loading
        self.tsize = tsize

        # loads maps and adapts them to the screen size
        make_maps(self.tsize)

        # loads all the walls from the map
        self.load_background(0)
        if background_sprite:
        
            self.background_sprite = graphic_engine.load_sprite(background_sprite)


    def run(self):
        
        # run all the objects and graphics
        self.graphic_engine.clear()

        for obj in Engine.instances:

            obj.run()
            obj.update_bbox()
            obj.draw_sprite()
            self.draw_background(0)
        
        self.graphic_engine.draw_map()


    def draw_background(self, id):
        
        # draw the background
        for i in MAPS[id]:

            self.graphic_engine.draw_rectangle(i[0], i[1], '#')
            self.graphic_engine.change_char(i[0][0], i[0][1], '=')
            self.graphic_engine.change_char(i[1][0], i[1][1], '=')


    def load_background(self, id):
        
        # load the background from the map
        for i in MAPS[id]:

            Wall([i[0][0], i[0][1], i[1][0], i[1][1]])



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
