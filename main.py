from game import Board

b = Board()

# only for testing purposes
while True:
    print('\n\n\n')
    b.play(int(input("choose column (1-7): ")) - 1)
    b.getBoard()
    if b.checkWin():
        print('player %i won' % b.turn)
        b.restart()
    else:
        b.changeTurn()
        print('player %i played' % b.turn)
