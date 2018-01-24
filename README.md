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
 ------------
|    ██████  |
|    ██      |
|            |
|            |
|            |
|            |
|            |
|            |
|            |
|            |
|            |
|            |
|            |
|            |
|            |
 ------------
#piece: 1   score: 0
```
You can use the following keys to control movement of the stone at each step:

- `l`: move left
- `r`: move right
- `t`: clockwise rotation for 90 degrees
- `n` or ` `: do nothing

## MineSweeper
To play the game, `cd` in to the MineSweeper folder, and run 

```python
# example 
python MineSweeper.py 15 15 20
```
The arguments are explained as following:

- usage: `MineSweeper.py [-h] R C Nmine`

- positional arguments:
  - `R`: number of rows for the game board (between [4, 26])
  - `C`: number of columns for the game board (between [4,26])
  - `Nmine`: number of mines
 
The mine zone is represented by a matrix with rows and columns labeled with letters. The letters will be used in commands to make your moves.

```python
   a b c d e f g h i j k l m n o
  ------------------------------
a|                     1 █ 1     |
b|                     1 █ 1     |
c| 2 2 1           1 1 2 1 1     |
d| F F 1           1 █ 1     1 1 |
e| █ 3 1           1 1 1     1 █ |
f| █ 1   1 1 1               2 █ |
g| 1 1   1 █ 1     1 2 2 1   1 █ |
h|       1 1 1     1 F F 1   1 1 |
i| 1 1             2 3 3 1       |
j| █ 1           1 2 F 1         |
k| █ 1 1 1 2 1 1 1 █ █ 1         |
l| █ █ █ █ █ █ █ █ █ █ 1         |
m| █ █ █ █ █ █ █ █ █ █ 1   1 1 1 |
n| █ █ █ █ █ █ █ █ 2 1 1   1 █ █ |
o| █ █ █ █ █ █ █ █ 1       1 █ █ |
  ------------------------------
Number of mines: 20
Number of flags: 5
```

You will see this prompt asking you for next move: `You next move (f/c row column):`   
There are two kinds of moves you can make:

- flag (syntax `f row col`)   
   for example: `f a c` will flag block row `a` and column `c` as mine (marked with a yellow `F`)
- click (syntax `c row col`)   
	for example: `c b e` will click on block row `e` column `f`. If it is a mine, game over. Otherwise, the number for that block will be disclosed.

When game is over, the full unmasked mine zone will be displayed, using red `M`s as mines:

```python
Game over!
   a b c d e f g h i j k l m n o
  ------------------------------
a|                     1 1 1     |
b|                     1 M 1     |
c| 2 2 1           1 1 2 1 1     |
d| M M 1           1 M 1     1 1 |
e| 3 3 1           1 1 1     1 M |
f| M 1   1 1 1               2 2 |
g| 1 1   1 M 1     1 2 2 1   1 M |
h|       1 1 1     1 M M 1   1 1 |
i| 1 1             2 3 3 1       |
j| M 1           1 2 M 1         |
k| 1 1 1 1 2 1 1 1 M 2 1         |
l|     1 M 2 M 1 1 2 2 1         |
m|     1 1 2 1 1   1 M 1   1 1 1 |
n|   1 1 2 1 1 1 1 2 1 1   1 M 1 |
o|   1 M 2 M 1 1 M 1       1 1 1 |
  ------------------------------
```
