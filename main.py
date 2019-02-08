from game import Board

b = Board()

# only for testing purposes
continueProgram = True
continueGame = True
while continueProgram:
    while continueGame:
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
                continueGame = False
            else:
                print('player %i played' % b.turn)
                b.changeTurn()
            print('\n\n\n')

    end = ''
    while end.upper() not in ['Y', 'N']:
        end = input("Would you like to play again (Y/N)? ")
    if end.upper() == 'N':
        continueProgram = False
        print("Thanks for playing!")
    else:
        continueGame = True
        b.restart()

