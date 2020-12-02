import random
import arcade

"""
Required Packages
arcade
numpy (note, if using python 3.9.0, use numpy version 1.19.3)
"""

#Constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Cellular Automata"
GRIDX = 160
GRIDY = 90


class Cell:
    """
    A simple cell class that stores the current state of the cell and can be printed as a * for alive and - for dead
    """
    def __init__(self,state):
        self.state = state
        self.lived = 0
        self.ID = random.random()

    def __str__(self):
        if self.state:
            return '*'
        else:
            return '-'

    def set_state(self,state):
        self.state=state
        if self.state:
            self.lived+=1

class Grid:
    """
    A class for the grid that creates a grid of cells of given size
    """
    def __init__(self,size):
        #create an empty grid
        self.g = self.make_grid(size)
        self.size = size
    def make_grid(self,size):
        #create an empty grid
        grid = []
        #for each row, make an empty inner list
        for row in range(size[0]):
            inner_list = []
            #for each item in that row, add a None
            for col in range(size[1]):
                inner_list.append(None)
            grid.append(inner_list)
        #replace all the Nones with Cells
        for row in range(size[0]):
            for col in range(size[1]):
                grid[row][col]=Cell(0)
            #this makes sure that all the Cells are unique objects
        return grid


    def __str__(self):
        """
        prints out the grid to look like
        *-*-*-
        -*-*-*
        ...
        where * is alive and - is dead
        """
        _str = ''
        for i in range(len(self.g[0])):
            for j in range(len(self.g[1])):
                _str+=str(self.g[i][j])
            _str+='\n'
        return _str
    def randomise(self):
        """
        Set up the grid to randomly turn on cells
        """
        for row in self.g:
            for cell in row:
                r = random.choice([0,1])
                cell.state = r


    def conway(self,steps):
        """
        Conway's game of life is a very famous set of rules for CA, it considers all 8 neighbours:
        if any alive cell has <2 alive neighbours, it dies
        if any alive cell has 2<=neighbours<3, it survives
        if any alive cell has >3 neighbours, it dies
        if any dead cell has neighbours = 3, it reproduces
        neighbours to cell [i][j] = [(i-1,j-1),(i-1,j),(i-1,j+1)
                                     (i,j-1),          ,(i,j+1)
                                     (i+1,j-1),(i+1,j),(i+1,j+1)]
        """
        #make a new empty grid
        new_grid = self.make_grid(self.size)
        #determine the number of neighbours each cell has
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                n = 0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if(x==i and y == j): #don't count yourself
                            pass
                        else:
                            if(x>=0 and y>=0 and x<len(self.g) and y<len(self.g[i])): #avoid out of range errors
                                n+=self.g[x][y].state
                if(n<2 or n>3): #if there's fewer than 2 neighbours or greater than 3, die
                    new_grid[i][j].state = 0
                elif(n>=2 and n<3): #if there's between 2 and 3 neighbours, continue as is
                    new_grid[i][j].state = self.g[i][j].state
                elif(n==3): #if there are 3 neighbours, live
                    new_grid[i][j].state = 1
        self.g = new_grid
                
    
class Display(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        self.shapes = arcade.ShapeElementList()
        self.grid = Grid([GRIDX,GRIDY])
        self.grid.randomise()
        self.steps = 0

    def draw_grid(self):
        """
        converts the grid to sprites to be drawn
        """
        RECT_WIDTH = SCREEN_WIDTH/GRIDX
        RECT_HEIGHT = SCREEN_HEIGHT/GRIDY
        shapeList = arcade.ShapeElementList()
        for row in range(GRIDX):
            for col in range(GRIDY):
                if self.grid.g[row][col].state:
                    rect = arcade.create_rectangle_filled(row*RECT_WIDTH,col*RECT_HEIGHT,RECT_WIDTH,RECT_HEIGHT,arcade.color.BLUE)
                    shapeList.append(rect)
        return shapeList
                    


    def on_update(self,delta_time):
        """
        update the grid
        """
        self.grid.conway(self.steps)
        self.steps+=1


    def on_draw(self):
        """
        call every time you want to draw to the screen
        """
        # Clear the screen and start drawing
        arcade.start_render()
        self.shapes = self.draw_grid()
        self.shapes.draw()
        

    
            

def main():
    d = Display()
    arcade.run()



if __name__ == "__main__":
    main()
