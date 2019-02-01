from game import Board
from random import randint

b = Board()

# only for testing purposes
while True:
    print('\n\n\n')
    b.play(int(input("choose column (1-7): ")) - 1)
    b.getBoard()
    if b.checkWin():
        print('player %i won' % b.turn)
        quit()
    b.changeTurn()
    print('player %i played' % b.turn)
