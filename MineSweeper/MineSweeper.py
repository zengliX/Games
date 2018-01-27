import argparse
import GameBoard
from curses import wrapper
import GameWindow
import curses

parser = argparse.ArgumentParser()
parser.add_argument('R', help='number of rows for the game board (between [4, 26])')
parser.add_argument('C',help='number of columns for the game board (between [4,26])')
parser.add_argument('Nmine',help='number of mines')
args = parser.parse_args()

def Gamerun(stdscr):
    """
    initiate interactive window
    """
    params = {
            'title_rows': 2,
            'window_size': (Game.nrow+2, Game.ncol*2+2),
            'status_rows': 6
            }
    window = GameWindow.Window(params,stdscr)
    window.set_title("MineSweeper.py: written by Li Zeng")
    
    """
    initiate color
    """
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
    
    
    """
    start game
    """
    while not Game.gameover():
        # print game state
        Game.summary(window)
        Game.print_mask(window)
        
        # check game win
        if Game.gamewin():
            window.set_status("You found all the mines! Press any button to exit ...",4)
            window.newKey()
            exit(0)
        
        # take user command
        user_input = Game.request_input(window)
        
        # process a valid command
        Game.proc_input(user_input,window)
        
    # if game over
    window.set_status("Game over. Press any button to exit ...",5)
    Game.summary_final(window)
    Game.print_unmask(window)
    window.newKey()
    window.closeWindow()

if __name__ == "__main__":
    # initialize game
    nrow = int(args.R)
    ncol = int(args.C)
    Nmine = int(args.Nmine)
    
    # initiate game
    Game = GameBoard.MineSweeperBoard(nrow,ncol,Nmine)
    
    # play game
    wrapper(Gamerun)
    
