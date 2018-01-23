import argparse
import GameBoard

parser = argparse.ArgumentParser()
parser.add_argument('R', help='number of rows for the game board (between [4, 26])')
parser.add_argument('C',help='number of columns for the game board (between [4,26])')
parser.add_argument('Nmine',help='number of mines')
args = parser.parse_args()

if __name__ == "__main__":
    # initialize game
    nrow = int(args.R)
    ncol = int(args.C)
    Nmine = int(args.Nmine)
    
    # initiate game
    Game = GameBoard.MineSweeperBoard(nrow,ncol,Nmine)
    
    # play game
    while not Game.gameover():
        # print game state
        #Game.print_unmask()
        Game.print_mask()
        Game.summary()
        
        # check game win
        if Game.gamewin():
            print("\nYou found all the mines!")
            exit(0)
        
        # take user command
        user_input = input("You next move (f/c row column):\n")
        
        # process a valid command
        Game.proc_input(user_input)
        
    # if game over
    print("\nGame over!")
    Game.print_unmask()
    Game.summary_final()
    
