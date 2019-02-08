from game import Board

b = Board()

# only for testing purposes
endProgram = False
endGame = False
while not endProgram:
    while not endGame:
        b.displayPlayer()
        try:
            col = input("choose column (1-7): ")
            col = int(col)
            assert 0 < col and col < 8
        except:
            print("Please enter a number from 1 to 7")
        else:
            b.play(int(col) - 1)
            b.getBoard()
            if b.checkWin():
                print('player %i won' % b.turn)
                b.restart()
            else:
                print('player %i played' % b.turn)
                b.changeTurn()
            print('\n\n\n')

    end = ''
    while end.upper() not in ['Y', 'N']:
        end = input("Would you like to play again (Y/N)? ")
    if end.upper() == 'N':
        endProgram = False

