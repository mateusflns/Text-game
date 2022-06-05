CURSOR_UP = '\033[1A'
CLEAR_LINE = '\x1b[2K'



class Char_map():


    def __init__(self, xsize, ysize) -> None:

        self.msize = [xsize, ysize] # size of map
        self.map = self.fill_map(' ') # map

    # Map manipulation
    def fill_map(self, char : str, size=False) -> None:
        '''
        Fills map with desired char
        '''
        if not size:
            size = self.msize
        return [[char]*size[0] for i in range(size[1])]


    def draw_map(self) -> None:
        '''
        Draws map to screen
        '''
        draw = ''
        for i in self.map:
            draw += ''.join(i)

        print(CURSOR_UP, end=CLEAR_LINE) 
        print(draw)


    def clear(self):
        '''
        Clears map
        '''
        self.map = self.fill_map(' ')


    def draw_circle(self, xc, yc, radius, line_width=2, char='*') -> None:
        '''
        Draws a circle to the map
        Circle will allways be offset to the right
        If outside of map, it will be cut off
        x, y : center of circle
        '''
        
        # offset on the x coord to correct for character height
        xoffset = 0
        x = radius*-1

        # offset on x origin to correct for the radius
        xc -= radius

        for i in range(radius*2 + 1):
        
            y = radius*-1
        
            for j in range(radius*2 +1):
                # circle equation
                # i don't know how it works :D
                edge = (x*x + y*y) / radius - radius
        
                # if edge is within the line width, draw the char
                if edge > -1*line_width*4/3 and edge < 1:
        
                    # if the char is outside of the map, cut it off
                    if not( x+xc < 0 or x+xc+xoffset+1 >= self.msize[0] or y+yc < 0 or y+yc >= self.msize[1]):
                        #draw characters
                        self.change_char(x+xoffset+xc, y+yc, char)        
                        #character offset by 1 to compensate the uneven terminal size
                        self.change_char(x+xoffset+xc+1, y+yc, char)        
        

                y += 1
        
        
            x+=1
            xoffset += 1



    def draw_line(self, cd1 : list, cd2 : list, char = '*') -> None:
        '''
        Draws a line from cd1 to cd2
        cd1 has to be the left most point
        '''
        x1, y1 = cd1
        x2, y2 = cd2
        dx = abs(x2 - x1)
        dy = -abs(y2 - y1)
        if x1 < x2: sx = 1 
        else : sx = -1
        if y1 < y2: sy = 1 
        else : sy = -1
        error = dx + dy

        while True:
            self.change_char(x1, y1, char)
            if x1 == x2 and y1 == y2: 
                break
            error2 = error * 2
            if error2 >= dy:
                if x1 == x2 :
                    break
                error += dy
                x1 += sx
            elif error2 <= dx:
                if y1 == y2 :
                    break
                error += dx
                y1 += sy
        

    def draw_rectangle(self, cd1 : list, cd2 : list, char = '*') -> None:
        '''
        Draws a rectangle from cd1 to cd2
        '''
        #drawing all lines
        self.draw_polyline([cd1, [cd1[0], cd2[1]], cd2, [cd2[0], cd1[1]], cd1], char)


    def draw_polyline(self, coords : list, char = '*') -> None:
        '''
        Draws a polyline from coords
        '''
        for i in range(len(coords)-1):
            self.draw_line(coords[i], coords[i+1], char)


    # char manipulation
    def change_char(self, x : int, y : int, char : str) -> None:    
        '''
        Changes char at x, y to char
        '''

        self.map[y][x] = char



