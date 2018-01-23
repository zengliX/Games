import Block
import numpy as np


    

class MineSweeperBoard:
    """
    game initiation
        nrow: number of rows
        ncol: number of columns
        Nmine: number of mines
        GOflag: gameover flag
    summary:
        Nflag: number of flags
        rightFlag: correct flag
        wrongFlag: wrong flag
        Nclick: number of clicks
    """
    def __init__(self,nrow, ncol, Nmine):
        assert nrow>=4 and ncol >=4 and nrow<=26 and ncol <= 26
        assert Nmine<= nrow*ncol

        ABC = 'abcdefghijklmnopqrstuvwxyz'
        self.nrow = nrow
        self.ncol = ncol
        self.Nmine = Nmine
        self.GOflag = False
        self.rowInd = ABC[:nrow]
        self.colInd = ABC[:ncol]
            
        # game board
        num_board  = np.zeros(nrow*ncol,dtype = 'int32')
        loc = np.random.choice(list(range(nrow*ncol)),size= Nmine,replace=False)
        num_board[loc] = 1
        num_board = num_board.reshape([nrow, ncol])
        self.initBoard(num_board)
        
        # game summary info
        self.Nflag = 0
        self.rightFlag = 0
        self.wrongFlag = 0
        self.Nclick = 0
    
    """
    used in __init__ to initialize board with corresponding to a binary array
    """
    def initBoard(self,arr):
        self.Board = []
        for i in range(self.nrow):
            onerow = []
            for j in range(self.ncol):
                if arr[i,j] == 1:
                    onerow.append(Block.Block(1,'M'))
                elif arr[i,j] == 0:
                    ct = self.count_mines(arr,i,j)
                    onerow.append(Block.Block(0,ct if ct>0 else ' '))
            self.Board.append(onerow)
        
    def count_mines(self,arr,r,c):
        ct = 0
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if i>=0 and i<self.nrow and j>=0 and j<self.ncol:
                    ct += arr[i,j]
        ct -= arr[r,c]
        return ct
            
    
    """
    process user input
    """
    def proc_input(self,msg):
        temp = msg.split(' ')
        # check command validity
        if len(temp) != 3: 
            self.input_err(msg)
            return
        action, r, c = temp
        if not self.valid_action(action) or not self.valid_block(r,c):
            self.input_err(msg)
            return
        
        # process valid command
        r_ind = self.rowInd.index(r)
        c_ind = self.colInd.index(c)            
        if action == 'f': # flag a block
            self.Board[r_ind][c_ind].MarkFlag(self)            
        if action == 'c': # click a block
            self.mem = set()
            self.DFS_click(r_ind,c_ind)
            if self.Board[r_ind][c_ind].value == 'M':
                self.GOflag = True
            
    def DFS_click(self,r_ind,c_ind):
        if (r_ind, c_ind) in self.mem: return
        
        self.mem.add((r_ind,c_ind))
        block = self.Board[r_ind][c_ind]
        block.click(self)
        if block.value != ' ': return
        # recursion when it is ' ' block
        for i in range(r_ind-1,r_ind+2):
            for j in range(c_ind-1,c_ind+2):
                if i>=0 and i<self.nrow and j>=0 and j<self.ncol:
                    self.DFS_click(i,j)
                    
    """
    check valid action
    """
    def valid_action(self,action):
        return action in ['f','c']
    
    """
    check valid block
    """
    def valid_block(self,r,c):
        return (r in self.rowInd) and (c in self.colInd)
    
    """
    print input error message
    """
    def input_err(self,msg):
        print("invalid command:", msg)
    
    
    """
    determine if game over/ win
    """
    def gameover(self):
        return self.GOflag
    
    def gamewin(self):
        return self.Nclick == self.nrow*self.ncol - self.Nmine

    """
    print game board, with mask
    """
    def print_mask(self):
        temp = ' '.join(list(self.colInd))
        print('   '+temp)
        print('  '+'--'*self.ncol)
        
        for i in range(self.nrow):
            print(self.rowInd[i]+'|',end='')
            for j in range(self.ncol):
                self.Board[i][j].print_mask()
            print(' |')
        print('  '+'--'*self.ncol)
        
    
    
    """
    print game board, without mask
    """
    def print_unmask(self):
        temp = ' '.join(list(self.colInd))
        print('   '+temp)
        print('  '+'--'*self.ncol)
        for i in range(self.nrow):
            print(self.rowInd[i]+'|',end='')
            for j in range(self.ncol):
                self.Board[i][j].print_unmask()
            print(' |')
        print('  '+'--'*self.ncol)
        

     
    """
    print game summary in game process, and when gameover
    """
    
    def summary(self):
        print("Number of mines:",self.Nmine)
        print("Number of flags:",self.Nflag)

    def summary_final(self):
        print("Number of mines:",self.Nmine)
        print("Number of clicked blocks:",self.Nclick)
        print("Number of flags:",self.Nflag)
        print("Number of correct flags:",self.rightFlag)
        print("Number of wrong flags:",self.wrongFlag)