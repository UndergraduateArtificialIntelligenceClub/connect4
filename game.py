class Board():
    def __init__(self):
        # creates 7x6 connect4 list of cells
        self.cells = [[0 for i in range(7)] for j in range(6)]
        # player1 starts first
        self.turn = 1
        self.characters = [' ', 'X', 'O']

    def displayPlayer(self):
        # returns formatted of information of the current player's turn and their token character
        print("player {:d} ({:s})".format(
            self.turn, self.characters[self.turn]))

    def displayBoard(self):
        # renders the board
        for row in self.cells:
            print('|', end='')
            for cell in row:
                print(self.characters[cell], end='|')
            print('\n', end='')

    def getBoard(self):
        # returns the cells 2d array of the board
        return self.cells

    def changeTurn(self):
        # Changes the turn of the players
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1

    def getTurn(self):
        # returns the current turn
        return self.turn

    def play(self, column):
        # this function will drop a token in a cell, given a column
        found = False
        row = len(self.cells) - 1
        while row >= 0 and not found:
            # starts from the bottom row and keeps going
            # upward until an empty cell is found
            cell = self.cells[row][column]
            if cell == 0:
                self.cells[row][column] = self.turn
                found = True
            else:
                row -= 1

    def isFull(self):
        # returns a boolean of wether the board is full or not
        for row in self.cells:
            for col in row:
                if col == 0:
                    return False
        return True

    def restart(self):
        # player1 starts first
        self.turn = 1
        # resets 7x6 grid to all 0
        self.cells = [[0 for i in range(7)] for j in range(6)]

    def checkWin(self):
        # checks for win for horizontal, vertical and diagonal conditions
        # returns True if a win is found
        return self.rowWin() or self.colWin() or self.diagWin()

    def rowWin(self):
        # checks for horizontal wins
        # returns True if a win is found
        for row in self.cells:
            for col in range(len(self.cells) - 3):
                if row[col] == self.turn and row[col + 1] == self.turn and row[col + 2] == self.turn and row[col + 3] == self.turn:
                    return True
        return False

    def colWin(self):
        # checks for vertical wins
        # returns True if a win is found
        for col in range(len(self.cells[0])):
            for row in range(len(self.cells) - 3):
                if self.cells[row][col] == self.turn and self.cells[row + 1][col] == self.turn and self.cells[row + 2][col] == self.turn and self.cells[row + 3][col] == self.turn:
                    return True
        return False

    def diagWin(self):
        # checks for diagonal wins (both directions)
        # returns True if a win is found

        # top-left to bottom-right
        for row in range(3):
            for col in range(4):
                if self.cells[row][col] == self.cells[row + 1][col + 1] == self.cells[row + 2][col + 2] == self.cells[row + 3][col + 3] == self.turn:
                    return True

        # top-right to bottom-left
        for row in range(3):
            for col in range(6, 2, -1):
                if self.cells[row][col] == self.cells[row + 1][col - 1] == self.cells[row + 2][col - 2] == self.cells[row + 3][col - 3] == self.turn:
                    return True

        # no win
        return False

    def colNotFull(self):
        # returns a list of the column indexes that aren't full
        # True: full
        # False: not full
        notFullList = []
        for col in range(7):
            # only checks for the top row since it can only
            # be filled uo if the rest is also filled up
            if self.cells[0][col] == 0:
                notFullList.append(col)
        return notFullList
