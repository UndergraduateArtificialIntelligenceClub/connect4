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

    def getBoard(self):
        # renders the board
        print('\n\n')
        for row in self.cells:
            print('|', end='')
            for col in row:
                print(col.printState(), end='|')
            print('\n', end='')

    def play(self, turn, column):
        found = False
        row = len(self.cells) - 1
        while row >= 0 and not found:
            cell = self.cells[row][column]
            if cell.getState() == 0:
                cell.changeState(turn)
                found = True
            else:
                row -= 1
