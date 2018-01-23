import argparse
from  gamestate import GameState

parser = argparse.ArgumentParser()
parser.add_argument('R', help='number of rows for the game board (>=5)')
parser.add_argument('C',help='number of columns for the game board (>=5)')
args = parser.parse_args()

if __name__ == "__main__":
    # initialize game
    nrow = int(args.R)
    ncol = int(args.C)
    Game = GameState(nrow,ncol)
    
    while not Game.gameover():
        """
        check if a new piece is needed
        if so, generate random piece, and reset needNew flag
        """
        if Game.RequestNew():
            cur_piece = Game.RandomPiece()
            #print("new piece generated:")
            #cur_piece.printPiece()
            #cur_piece.printInfo()
            Game.needNew = False
            # if cur_piece not valid, then game over
            if not Game.ValidPiece(cur_piece):
                Game.printWithPiece(cur_piece)
                break
        
        """
        print the game with piece overlay
        """
        Game.printWithPiece(cur_piece)
        
        """
        ask for movement direction when it can move down
        otherwise, fix the piece to board, and rest needNew flag
        """
        if Game.ValidMove(cur_piece,'d'):
            mv = input("Next move: (l(left)/r(right)/n(None)/t(turn clockwise))\n")
            if not Game.ValidMove(cur_piece, mv):
                print("Invalid move:", mv)
            else:
                cur_piece = cur_piece.makeMove(mv)
            if Game.ValidMove(cur_piece,'d'):
                cur_piece = cur_piece.makeMove('d')
        else:
            print("fixing the piece")
            Game.addPiece(cur_piece)
            Game.fullRow()
            Game.needNew = True
            
    print("\nGame Over.")
    
