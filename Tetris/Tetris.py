import argparse
from  gamestate import GameState
import GameWindow
from curses import wrapper

parser = argparse.ArgumentParser()
parser.add_argument('R', help='number of rows for the game board (>=5)')
parser.add_argument('C',help='number of columns for the game board (>=5)')
args = parser.parse_args()


def GameRun(stdscr):
    """
    initiate interactive window
    """
    params = {
            'title_rows': 2,
            'window_size': (Game.nrow+2, Game.ncol*2+2),
            'status_rows': 3
            }
    window = GameWindow.Window(params,stdscr)
    window.set_title("Tetris.py: written by Li Zeng")
    
    """
    start game
    """
    while not Game.gameover() and window.key() != 27:
        """
        check if a new piece is needed
        if so, generate random piece, and reset needNew flag
        """
        if Game.RequestNew():
            cur_piece = Game.RandomPiece()
            Game.needNew = False
            # if cur_piece not valid, then game over
            if not Game.ValidPiece(cur_piece):
                break
        
        """
        print the game with piece overlay
        """
        Game.print_to_window(window,cur_piece)
        
        """
        ask for movement direction when it can move down
        otherwise, fix the piece to board, and rest needNew flag
        """        
        if Game.ValidMove(cur_piece,'d'):
            # request a movement
            window.set_status("Use the direction button to move the stone (up:rotation)",1)
            Game.print_to_window(window,cur_piece)
            # process new movement
            window.newKey()
            mv = Game.keymap.get(window.key(),' ')
            if not Game.ValidMove(cur_piece, mv):
                window.set_status("Invalid move.",2)
            else:
                window.set_status('',2)
                cur_piece = cur_piece.makeMove(mv)
            if Game.ValidMove(cur_piece,'d'):
                cur_piece = cur_piece.makeMove('d')
        else:
            window.set_status('',2)
            Game.addPiece(cur_piece)
            Game.fullRow()
            Game.needNew = True
        
    
    window.set_status("Game Over. Press any key to exit.",2)
    Game.print_to_window(window, cur_piece)
    window.newKey()
    window.closeWindow()


if __name__ == "__main__":
    # initialize game
    nrow = int(args.R)
    ncol = int(args.C)
    Game = GameState(nrow,ncol)
    wrapper(GameRun)
    
    
