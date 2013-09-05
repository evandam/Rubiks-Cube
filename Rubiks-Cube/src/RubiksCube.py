'''
Created on Sep 5, 2013

@author: Evan
'''

class Cube:
    '''
    A representation of a 3x3 Rubik's Cube
    '''


    def __init__(self):
        '''
        Initialize the cube in solved state.
        Each side is a 2D array that has a facing color.
        '''
        self.top    = [[['R'] * 3] * 3]
        self.bottom = [[['O'] * 3] * 3]
        self.left   = [[['Y'] * 3] * 3]
        self.right  = [[['G'] * 3] * 3]
        self.front  = [[['B'] * 3] * 3]
        self.back   = [[['W'] * 3] * 3]
        
    def printSide(self, side):
        '''
        Representation of one side of the cube
        '''
        for row in side:
            for col in row:
                print col
                
    def printCube(self):
        '''
        Representation of the entire cube (prints all sides)
        '''
        for side in [self.top, self.bottom, self.left, self.right, self.front, self.back]:
            self.printSide(side)
            print ''
        
    def rotateX(self, x):
        '''
        Make one clockwise(?) rotation for the given row.
        '''
        pass
    
    def rotateY(self, y):
        '''
        Make one clockwise(?) rotation for the given column.
        '''
        pass
    
if __name__ == '__main__':
    cube = Cube()
    cube.printCube()
        