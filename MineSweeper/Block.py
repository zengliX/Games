from colorama import init, Fore
init(autoreset=True)

ColorMap = {1:Fore.WHITE, 2:Fore.GREEN, 3:Fore.CYAN, 4:Fore.LIGHTYELLOW_EX, \
            5: Fore.MAGENTA, 6:Fore.MAGENTA, 7:Fore.RED, 8:Fore.RED, ' ':Fore.BLACK}

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
    print with mask
    """
    def print_mask(self):
        if self.flag:
            print(Fore.YELLOW+' '+'F',end='')
        elif self.mask:
            print(' '+chr(9608),end='')
        else:
            print(ColorMap[self.value]+' '+str(self.value),end='')
    
    """
    print without mask
    """
    def print_unmask(self):
        if self.mine:
            print(Fore.RED+' '+str(self.value),end='')
        else:
            print(ColorMap[self.value]+' '+str(self.value),end='')