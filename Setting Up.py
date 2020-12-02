import random
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
        self.g = []
        #for each row, make an empty inner list
        for row in range(size[0]):
            inner_list = []
            #for each item in that row, add a None
            for col in range(size[1]):
                inner_list.append(None)
            self.g.append(inner_list)
        #replace all the Nones with Cells
        for row in range(size[0]):
            for col in range(size[1]):
                self.g[row][col]=Cell(0)
            #this makes sure that all the Cells are unique objects
    
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
    

    
            

def main():
    grid = Grid([25,25])


if __name__ == "__main__":
    main()
