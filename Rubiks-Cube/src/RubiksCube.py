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
        Each side is a 2D array that has a facing color.
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
        
        # better name for sides? all kind of depends on the perspective...
        self.top, self.bottom, self.left, self.right, self.front, self.back = [], [], [], [], [], []
        
        with open(fp, 'r') as f:
            lines = [line.replace(' ', '').strip() for line in f.readlines()]
        
        self.back   = [list(lines[x])       for x in range(3)]
        self.left   = [list(lines[x][:3])   for x in range(3, 6)]
        self.bottom = [list(lines[x][3:6])  for x in range(3, 6)]
        self.right  = [list(lines[x][6:9])  for x in range(3, 6)]
        self.front  = [list(lines[x])       for x in range(6, 9)]
        self.top    = [list(lines[x])       for x in range(9, 12)]
        
        
    def __str__(self):
        ''' Format back to input file '''
        
        toString = ''
        for row in self.back:
            ''' pad with spaces and print each row on the side '''
            toString += '   %s\n' % (''.join(row))
            
        for row in range(3):
            ''' print 3 sides together '''
            toString += ''.join(self.left[row])
            toString += ''.join(self.bottom[row])
            toString += ''.join(self.right[row])
            toString+= '\n'
        
        for row in self.front:
            toString += '   %s\n' % (''.join(row))
            
        for row in self.top:
            toString += '   %s\n' % (''.join(row))
                
        return toString
            
        
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
    
        