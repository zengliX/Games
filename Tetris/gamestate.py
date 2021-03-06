import numpy as np
from piece import Piece
import curses

class GameState:
    def __init__(self,r,c):
        self.createBoard(r,c)
        self.nrow = r
        self.ncol = c
        self.needNew = True
        self.Nshape = 19
        self.validmoves = set(['l','r','d','t'])
        # score related
        self.score = 0
        self.ct_piece = 0
        self.keymap = {curses.KEY_LEFT:'l', curses.KEY_RIGHT:'r', curses.KEY_DOWN:'d', curses.KEY_UP:'t'}
        
    def createBoard(self,r,c):
        assert r>5 and c>5
        self.Board = [[0 for i in range(c)] for j in range(r)]
    
    def gameover(self):
        return False
    
    def RequestNew(self):
        return self.needNew
    
    def RandomPiece(self):
        coord_r = 3
        coord_c = np.random.randint(self.ncol-4)
        shape = np.random.randint(self.Nshape)
        p = Piece(coord_r,coord_c,shape)
        self.ct_piece += 1
        return p
    
    """
    check if a piece can be put on board
    """
    def ValidPiece(self,p):
        for i in range(4):
            for j in range(4):
                if p.pieceBoard[i][j]==1:
                    if p.row-3+i<0 or p.row-3+i>=self.nrow or p.col+j<0 or p.col+j>=self.ncol:
                        return False
                    if self.Board[p.row-3+i][p.col+j]==1:
                        return False
        return True
    
    """
    test if a move is valid
    p: the working piece
    move: move command
    """
    def ValidMove(self,p,move):
        if not move in self.validmoves:
            return False
        else:
            new_piece = p.makeMove(move) 
            return self.ValidPiece(new_piece)
    
    """
    fix a piece to game board
    """
    def addPiece(self,p):
        for i in range(4):
            for j in range(4):
                if p.pieceBoard[i][j]==1:
                    self.Board[p.row-3+i][p.col+j]=1
    
    """
    check and handle full rows
    """
    def fullRow(self):
        ind = set()
        for i in range(self.nrow):
            if self.onerowfull(i):
                ind.add(i)
        if len(ind)>0:
            self.score += 100*len(ind)
            new_board = [[0]*self.ncol for i in range(len(ind))]
            new_board += [self.Board[i] for i in range(self.nrow) if not i in ind]
            self.Board = new_board
        
    def onerowfull(self,i):
        for j in range(self.ncol):
            if self.Board[i][j]==0:
                return False
        return True
    
    """
    print the piece overlay on the board
    p: a Piece object
    """
    """
    def printWithPiece(self,p):
        print()
        print(' '+'-'*2*self.ncol+' ')
        for i in range(self.nrow):
            print('|',end='')
            for j in range(self.ncol):
                # overlapping part
                if i-p.row<=0 and p.row-i<=3 and j-p.col>=0 and j-p.col<=3:
                    val = self.Board[i][j] + p.pieceBoard[i-p.row+3][j-p.col]
                    print('  ' if val==0 else chr(9608)*2, end='')
                else: # game board only part
                    print('  ' if self.Board[i][j]==0 else chr(9608)*2, end='')
            print('|')
        print(' '+'-'*2*self.ncol+' ')
    """
    
    """
    print Game to GameWindow
    GW: a gameWindow object
    p: a piece
    """
    def print_to_window(self,GW,p):
        GW.erase() # clear page
        # print title and status
        GW.set_status("#piece: %d   score: %d" %(self.ct_piece, self.score),0)
        GW.show() 
        # print board
        row_start = (GW.width-1)//2 - self.ncol-1
        GW.add(GW.window_start-1, row_start, ' '+'-'*2*self.ncol+' ')
        for i in range(self.nrow):
            row_ind = GW.window_start+i # row index
            GW.add(row_ind,row_start,'|')
            for j in range(self.ncol):
                if i-p.row<=0 and p.row-i<=3 and j-p.col>=0 and j-p.col<=3:  # overlapping part
                    val = self.Board[i][j] + p.pieceBoard[i-p.row+3][j-p.col]
                    GW.add( row_ind, 2*j+1+row_start, '  ' if val==0 else chr(9608)*2)
                else: # game board only part
                    GW.add( row_ind, 2*j+1+row_start, '  ' if self.Board[i][j]==0 else chr(9608)*2)
            GW.add(row_ind, 2*self.ncol+1+row_start,'|')
        GW.add(GW.window_start+self.nrow, row_start, ' '+'-'*2*self.ncol+' ')
        # move cursor
        GW.stdscr.move(0,0)