"""
Piece class:
class for each randomly generate Tetris piece
"""

PieceMap = {
        0: [[0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]],
            
        1: [[0,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0]],
            
        2: [[1,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]],
            
        3: [[0,1,1,0],
            [0,0,1,1],
            [0,0,0,0],
            [0,0,0,0]],
            
        4: [[0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0]],
        
        5: [[0,0,1,1],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]],
        
        6: [[0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,0,0]],
            
        7: [[0,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,0,0]],
        
        8: [[0,1,1,1],
            [0,1,0,0],
            [0,0,0,0],
            [0,0,0,0]],
        
        9: [[0,1,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,0,0]],
        
        10: [[0,0,1,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0]],
        
        11: [[0,0,1,0],
            [0,0,1,0],
            [0,1,1,0],
            [0,0,0,0]],
        
        12: [[0,1,0,0],
            [0,1,1,1],
            [0,0,0,0],
            [0,0,0,0]],
        
        13: [[0,1,1,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,0,0,0]],
        
        14: [[0,1,1,1],
            [0,0,0,1],
            [0,0,0,0],
            [0,0,0,0]],
            
        15: [[0,0,1,0],
            [0,1,1,1],
            [0,0,0,0],
            [0,0,0,0]],
             
        16: [[0,0,1,0],
            [0,0,1,1],
            [0,0,1,0],
            [0,0,0,0]],
        
        17: [[0,0,0,0],
            [0,1,1,1],
            [0,0,1,0],
            [0,0,0,0]],
        
        18: [[0,0,1,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,0,0]],
        }

RotationMap={0:0, 1:2, 2:1, 3:4, 4:3, 5:6, 6:5, 7:8, 8:9, 9:10, 10:7, \
             11:12, 12:13, 13:14, 14:11, 15:16, 16:17, 17:18, 18:15}

class Piece:
    """
    coord_r: row coordinate
    coord_c: column coordinate
    """
    def __init__(self, coord_r, coord_c, shape):
        self.row = coord_r
        self.col = coord_c
        self.shape = shape
        self.pieceBoard = PieceMap[shape]
    
    """
    return a piece after movement
    """
    def makeMove(self,move):
        if move == 'l':
            p = Piece(self.row, self.col-1, self.shape)
        elif move == 'r':
            p = Piece(self.row,self.col+1,self.shape)
        elif move == 'd':
            p = Piece(self.row+1,self.col,self.shape)
        elif move == 't':
            p = Piece(self.row, self.col,RotationMap[self.shape])
        elif move == 'n' or move == '':
            return self
        return p
    
    """
    piece info
    """
    def printInfo(self):
        print("row: %d, col: %d, shape: %d" % (self.row, self.col, self.shape))
    
    """
    print a grid representation of a piece
    """
    def printPiece(self):
        for i in range(4):
            print( ''.join([ '  ' if x==0 else chr(9608)*2 \
                            for x in self.pieceBoard[i] ]) )
        print()