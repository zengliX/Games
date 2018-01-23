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

