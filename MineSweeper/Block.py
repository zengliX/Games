"""
ColorMap:
    map numbers to colors specified in MineSweeper.py
"""
ColorMap = {1:1, 2:1, 3:2, 4:3, \
            5:3 , 6:4, 7:4, 8:4, ' ':6,'block':6,'F':4}

class Block:
    """
    initialize parameters
        val: 'M' for mine; number for #mines in neighborhood; ' ' for no mines around
        mask: whether the block is masked
        flag: whether the block is flagged
        mine: whether it is a mine
    """
    def __init__(self, ismine, val):
        self.value = val
        self.mask = True
        self.flag = False
        self.mine = True if ismine==1 else False
    
    """
    click a block
    """
    def click(self,Game):
        if self.mask:
            Game.Nclick += 1
            self.mask = False
    
    """
    flag/unflag a block
    """
    def MarkFlag(self,Game):
        self.flag = not self.flag
        if self.flag:
            Game.Nflag += 1
            if self.mine:
                Game.rightFlag += 1
            else:
                Game.wrongFlag += 1
        else:
            Game.Nflag -= 1
            if self.mine:
                Game.rightFlag -= 1
            else:
                Game.wrongFlag -= 1
    
    """
    str with mask
    """
    def str_mask(self):
        if self.flag:
            return(' '+'F',ColorMap['F'])
        elif self.mask:
            return(' '+chr(9608),ColorMap['block'])
        else:
            return(' '+str(self.value),ColorMap[self.value])
    
    """
    str without mask
    """
    def str_unmask(self):
        if self.mine:
            return(' '+str(self.value),ColorMap[8])
        else:
            return(' '+str(self.value),ColorMap[self.value])
            