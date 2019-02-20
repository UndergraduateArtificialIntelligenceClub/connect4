import os

class Board:
    def __init__(self, player1, player2):
        # creates 7x6 2-dimensional array representing the game state
        # cell = state[row][column]
        self.state = [[0 for column in range(7)] for row in range(6)]

        # 1 = player 1 turn, 2 = player 2 turn
        # player 1 starts
        self.turn = 1

        # used when printing the board
        self.characters = [' ', 'X', 'O']

        # player objects
        self.player1 = player1
        self.player2 = player2

    
    def playGame(self):
        # plays the game until a draw or win

        # reset the board and turn
        self.reset()

        # # testing
        # self.state=[
        #     [0,2,1,1,0,0,0],
        #     [0,1,2,2,0,0,0],
        #     [1,2,1,2,1,0,0],
        #     [2,1,1,2,1,0,0],
        #     [2,1,1,1,2,0,0],
        #     [1,2,2,2,1,2,0]
        # ]
        # self.turn = 2

        # game loop
        while True:
            # clear terminal
            os.system("clear")

            self.displayBoard()

            # check whether the game is over
            win = self.checkWin()

            if win == 0:
                print("   Draw!\n")
                break
            elif win == 1:
                print("   Player 1 wins!\n")
                break
            elif win == 2:
                print("   Player 2 wins!\n")
                break

            # game not over, so get the current player's move
            print("   Player {}'s turn.".format(self.turn))

            # call the current player's play function 
            # play functions are standardized for ease of adding new players
            if self.turn == 1:
                move = self.player1.play(self.state)
            else:
                move = self.player2.play(self.state)

            # make the chosen move
            self.play(move)

            self.changeTurn()

    def displayBoard(self):
        # prints out the board all pretty like
        # ex: -----------------------------
        #     | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
        #     -----------------------------
        #     |   |   |   | O |   | X |   |
        #     |   |   | X | O |   | O |   |
        #     |   |   | X | X |   | X | O |
        #     |   |   | O | X | O | O | X |
        #     | O | X | O | X | O | O | O |
        #     | X | O | X | O | X | X | X |
        #     -----------------------------

        print()
        print("   -----------------------------   ")
        print("   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |   ")
        print("   -----------------------------   ")
        for row in self.state:
            print("   |", end='')
            for cell in row:
                print(" {} |".format(self.characters[cell]), end='')
            print()
        print("   -----------------------------   ")
        print()

    def changeTurn(self):
        # Changes the turn of the players
        self.turn = 3 - self.turn

    def play(self, column):
        # this function will drop a token in a cell, given a column
        assert(self.state[0][column] == 0)
        for row in range(5, -1, -1):
            # starts from the bottom row and keeps going
            # upward until an empty cell is found
            if self.state[row][column] == 0:
                self.state[row][column] = self.turn
                break

    def checkWin(self):
        # checks for wins or draws
        # return values:
        # -1 = game not over
        # 0  = draw
        # 1  = player 1 win
        # 2  = player 2 win

        # check horizontal wins
        for row in range(6):
            for col in range(4):
                if self.state[row][col] == self.state[row][col + 1] == self.state[row][col + 2] == self.state[row][col + 3] and self.state[row][col] != 0:
                    return self.state[row][col]

        # check vertical wins
        for col in range(7):
            for row in range(3):
                if self.state[row][col] == self.state[row + 1][col] == self.state[row + 2][col] == self.state[row + 3][col] and self.state[row][col] != 0:
                    return self.state[row][col]

        # check diagonal top-left to bottom-right wins
        for row in range(3):
            for col in range(4):
                if self.state[row][col] == self.state[row + 1][col + 1] == self.state[row + 2][col + 2] == self.state[row + 3][col + 3] and self.state[row][col] != 0:
                    return self.state[row][col]

        # check diagonal bottom-left to top-right wins
        for row in range(3):
            for col in range(6, 2, -1):
                if self.state[row][col] == self.state[row + 1][col - 1] == self.state[row + 2][col - 2] == self.state[row + 3][col - 3] and self.state[row][col] != 0:
                    return self.state[row][col]

        # check draw
        if 0 not in self.state[0]:
            return 0
        
        # no win or draw
        return -1

    def reset(self):
        # resets the game

        # creates 7x6 connect4 list of cells
        self.state = [[0 for i in range(7)] for j in range(6)]
        # 1 = player 1 turn, 2 = player 2 turn
        self.turn = 1
    