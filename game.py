class Cell():
    def __init__(self):
        # state = 0: empty
        # state = 1: player1
        # state = 2: player2
        self.state = 0

    def getState(self):
        return self.state

    def printState(self):
        if self.state == 0:
            return '_'
        elif self.state == 1:
            return 'X'
        else:
            return 'O'

    def changeState(self, newState):
        if self.state == 0:
            self.state = newState


class Board():
    def __init__(self):
        # creates 7x6 connect4 list of cells
        self.cells = [[Cell() for i in range(7)] for j in range(6)]
        # player1 starts first
        self.turn = 1

    def getBoard(self):
        # renders the board
        for row in self.cells:
            print('|', end='')
            for col in row:
                print(col.printState(), end='|')
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
            if cell.getState() == 0:
                cell.changeState(self.turn)
                found = True
            else:
                row -= 1

    def checkWin(self):
        return self.rowWin() or self.colWin()

    def rowWin(self):
        for row in self.cells:
            for col in range(len(self.cells) - 3):
                if row[col].getState() == self.turn and row[col + 1].getState() == self.turn and row[col + 2].getState() == self.turn and row[col + 3].getState() == self.turn:
                    return True
        return False

    def colWin(self):
        for col in range(len(self.cells[0])):
            for row in range(len(self.cells) - 3):
                if self.cells[row][col].getState() == self.turn and self.cells[row + 1][col].getState() == self.turn and self.cells[row + 2][col].getState() == self.turn and self.cells[row + 3][col].getState() == self.turn:
                    return True
        return False
