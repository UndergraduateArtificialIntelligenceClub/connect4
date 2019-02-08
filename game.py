class Board():
    def __init__(self):
        # creates 7x6 connect4 list of cells
        self.cells = [[0 for i in range(7)] for j in range(6)]
        # player1 starts first
        self.turn = 1
        self.characters = [' ', 'X', 'O']

    def displayPlayer(self):
        print("player {:d} ({:s})".format(self.turn, self.characters[self.turn]))


    def getBoard(self):
        # renders the board
        for row in self.cells:
            print('|', end='')
            for cell in row:
                print(self.characters[cell], end='|')
            print('\n', end='')

    def changeTurn(self):
        # Changes the turns 
        # of the players
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1

    def play(self, column):
        found = False
        row = len(self.cells) - 1
        while row >= 0 and not found:
            cell = self.cells[row][column]
            if cell == 0:
                self.cells[row][column] = self.turn
                found = True
            else:
                row -= 1

    def isFull(self):
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
        return self.rowWin() or self.colWin() or self.diagWin()

    def rowWin(self):
        for row in self.cells:
            for col in range(len(self.cells) - 3):
                if row[col] == self.turn and row[col + 1] == self.turn and row[col + 2] == self.turn and row[col + 3] == self.turn:
                    return True
        return False

    def colWin(self):
        for col in range(len(self.cells[0])):
            for row in range(len(self.cells) - 3):
                if self.cells[row][col] == self.turn and self.cells[row + 1][col] == self.turn and self.cells[row + 2][col] == self.turn and self.cells[row + 3][col] == self.turn:
                    return True
        return False

    # Check diagonal wins, returns true if current player won, false otherwise
    def diagWin(self):
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
