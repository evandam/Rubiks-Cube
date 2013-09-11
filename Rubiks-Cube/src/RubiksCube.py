'''
Created on Sep 5, 2013

@author: Evan
'''

class Cube(object):
    '''
    A representation of a 3x3 Rubik's Cube
    '''
    
    def __init__(self, fp):
        '''
        Each side is a 2D array that has a color.
        Initialize the cube from a file formatted like: (spaces ignored)
                   RRR
                   RRR
                   RRR
                GGGYYYBBB
                GGGYYYBBB
                GGGYYYBBB
                   OOO
                   OOO
                   OOO
                   WWW
                   WWW
                   WWW
        '''
        
        ''' Each side of the cube - named for its center cubie '''
        self.red, self.green, self.yellow, self.blue, self.orange, self.white = [], [], [], [], [], []
        
        with open(fp, 'r') as f:
            lines = [line.replace(' ', '').strip() for line in f.readlines()]
        
        self.red    = [list(lines[x])       for x in range(3)]
        self.green  = [list(lines[x][:3])   for x in range(3, 6)]
        self.yellow = [list(lines[x][3:6])  for x in range(3, 6)]
        self.blue   = [list(lines[x][6:9])  for x in range(3, 6)]
        self.orange = [list(lines[x])       for x in range(6, 9)]
        self.white  = [list(lines[x])       for x in range(9, 12)]
        
        
    def __str__(self):
        ''' Format white to input file '''
        
        toString = ''
        for row in self.red:
            ''' pad with spaces and print each row on the side '''
            toString += '   %s\n' % (''.join(row))
            
        for row in range(3):
            ''' print 3 sides together '''
            toString += ''.join(self.green[row])
            toString += ''.join(self.yellow[row])
            toString += ''.join(self.blue[row])
            toString+= '\n'
        
        for row in self.orange:
            toString += '   %s\n' % (''.join(row))
            
        for row in self.white:
            toString += '   %s\n' % (''.join(row))
                
        return toString
    
    def isValid(self):
        '''
        Note that the six center faces are always the same in any valid state
        '''
        if self.red[1][1] != 'R':
            return False
        elif self.green[1][1] != 'G':
            return False
        elif self.yellow[1][1] != 'Y':
            return False  
        elif self.blue[1][1] != 'B':
            return False  
        elif self.orange[1][1] != 'O':
            return False  
        elif self.white[1][1] != 'W':
            return False  
        else:
            return True
              
        
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
#     cube = Cube('state.txt')
#     print cube
    
    solved = Cube('solved.txt')
    print solved
    print solved.isValid()
    
        