class Board():
    def __init__(self):
        # creates 7x6 connect4 list of cells
        self.cells = [[0 for i in range(7)] for j in range(6)]
        # player1 starts first
        self.turn = 1

        self.characters = [' ', 'X', 'O']

    def getBoard(self):
        # renders the board
        for row in self.cells:
            print('|', end='')
            for cell in row:
                print(self.characters[cell], end='|')
            print('\n', end='')

    def changeTurn(self):
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

    def checkWin(self):
        return self.rowWin() or self.colWin()

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
