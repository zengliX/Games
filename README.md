Some simple games written in Python3.

## Tetris

To play the game, `cd` in to the Tetris folder, and run 

```python
# example 
python Tetris.py 15 7
```
command line arguments are explained as the following: 

- usage: `Tetris.py [-h] R C`
- positional arguments:
  - `R`: number of rows for the game board (>=5)
  - `C`: number of columns for the game board (>=5)

After running the command, the game would start with a random stone, eg:

```python
Tetris.py: 
                      --------------
                     |              |
                     |    ██████    |
                     |      ██      |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                     |              |
                      --------------

#piece: 1   score: 0
Use the direction button to move the stone (up:rotation)
```
You can use the direction keys on your keyboar to control movements of the stone at each step. `KEY_UP` will rotate stone 90 degrees clockwise.


## MineSweeper
To play the game, `cd` in to the MineSweeper folder, and run 

```python
# example 
python MineSweeper.py 7 7 10
```
The arguments are explained as following:

- usage: `MineSweeper.py [-h] R C Nmine`

- positional arguments:
  - `R`: number of rows for the game board (between [4, 26])
  - `C`: number of columns for the game board (between [4,26])
  - `Nmine`: number of mines
 
The mine zone is represented by a matrix with rows and columns labeled with letters. The letters will be used in commands to make your moves.

```python
MineSweeper.py: 
                              a b c d e f g
                             --------------
                           a|     1 F 1     |
                           b| 2 2 3 2 2     |
                           c| █ █ █ F 1     |
                           d| █ █ █ 1 1     |
                           e| █ █ █ 1       |
                           f| █ █ █ 1   1 1 |
                           g| █ █ █ 1   1 F |
                             --------------
Number of mines: 10
Number of flags: 3
your next move, in the format of (f/c row col). f for flag, c for click.
your input: (_, _, _)
```

You will see this prompt asking you for next move: `You next move (f/c row column):`   
There are two kinds of moves you can make:

- flag (syntax `f row col`)   
   for example: `f a c` will flag block row `a` and column `c` as mine (marked with a yellow `F`)
- click (syntax `c row col`)   
	for example: `c b e` will click on block row `e` column `f`. If it is a mine, game over. Otherwise, the number for that block will be disclosed.

When game is over, the full unmasked mine zone will be displayed, using red `M`s as mines:

```python
MineSweeper.py: 
                              a b c d e f g
                             --------------
                           a|     1 M 1     |
                           b| 2 2 3 2 2     |
                           c| M M 3 M 1     |
                           d| 3 M 3 1 1     |
                           e| 2 3 3 1       |
                           f| 3 M M 1   1 1 |
                           g| M M 3 1   1 M |
                             --------------
Number of mines: 10
Number of flags: 3
Number of clicked blocks: 33
Number of correct flags: 3
Number of wrong flags: 0
Game over. Press any button to exit ...
```
