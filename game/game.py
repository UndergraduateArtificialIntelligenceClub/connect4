import os

class Board:
    def __init__(self, player1, player2):

        # creates 7x6 connect4 list of cells
        self.state = [[0 for i in range(7)] for j in range(6)]

        # 1 = player 1 turn, 2 = player 2 turn
        self.turn = 1

        self.characters = [' ', 'X', 'O']

        self.player1 = player1
        self.player2 = player2

    def playGame(self):
        while True:
            os.system("clear")

            self.displayBoard()

            win = self.checkWin()
            if win == 0:
                print("   Draw!")
                print()
                quit()
            elif win == 1:
                print("   Player 1 wins!")
                print()
                quit()
            elif win == 2:
                print("   Player 2 wins!")
                print()
                quit()

            print("   Player {}'s turn.".format(self.turn))

            if self.turn == 1:
                move = self.player1.play(self.state)
            else:
                move = self.player2.play(self.state)

            self.play(move)

            self.changeTurn()

    def displayBoard(self):
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

    def getState(self):
        # returns the cells 2d array of the board
        return self.state

    def changeTurn(self):
        # Changes the turn of the players
        self.turn = 3 - self.turn

    def getTurn(self):
        # returns the current turn
        return self.turn

    def play(self, column):
        # this function will drop a token in a cell, given a column
        assert(self.state[0][column] == 0)
        for row in range(5, -1, -1):
            # starts from the bottom row and keeps going
            # upward until an empty cell is found
            if self.state[row][column] == 0:
                self.state[row][column] = self.turn
                break

    def isFull(self):
        # returns a boolean of wether the board is full or not
        for row in self.state:
            for col in row:
                if col == 0:
                    return False
        return True

    def checkWin(self):
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

    def restart(self):
        # player1 starts first
        self.turn = 1
        # resets 7x6 grid to all 0
        self.state = [[0 for i in range(7)] for j in range(6)]
