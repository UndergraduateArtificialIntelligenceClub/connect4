Connect 4 Terminal Game Documentation
===
### Contributors
+ Giancarlo Pernudi Segura
+ Will Fenton
+ Paul Saunders

This connect 4 game is part of the Undergraduate Artificial Intelligence Society at the University of Alberta. It is licensed under the **GNU GENERAL PUBLIC LICENSE**.

## Board Class

This class contains the cells and the players. The interaction with the cells and players happens through this class. It has the following variables.

+ `cells`: a 2d array of integers representing the current game state (6x7)
+ `turn`: dictates which player's turn it is
+ characters: a dictionary for characters corresponding to an integer (0-2)
+ `player1`: either human, randomBot or smartBot
+ `player2`: either human, randomBot or smartBot

The class has the folllowing methods:
```{python}
playGame() # plays the game until there is a win or draw
player's turn and their token character
displayBoard() # prints out a graphical representation of the board
changeTurn() # alternates the turn between 1 and 2
play() # takes as input the index of column and plays
checkWin() # checks for possible win in all directions (vertical, horizontal, and diagonal)
reset() # resets the board for a new game
```

# Players
The player classes all have a `play()` funciton. It takes the `state` of the board as input. This does not mean it is used by each different player class
## HumanPlayer
This is the player object for a human. It does not use the `state` parameter for the `play()` function.
## RandomPlayer
This is the player object for a computer that plays randomly. Uses the `state` parameter to get a list of possible moves. It then chooses randomly form that list.
## MinimaxPlayer
This is the player object which uses a minimax algorithm to play.
`Now Will gets the joy of documenting this part cuz I'm too lazy`