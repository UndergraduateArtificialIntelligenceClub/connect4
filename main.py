from game import Board
from players import DumbBot

b = Board()
bot = DumbBot()

# only for testing purposes
while True:
    print('\n\n\n')
    b.displayPlayer()
    b.displayBoard()
    if b.getTurn() == 1:
        b.play(int(input("choose column (1-7): ")) - 1)
    elif b.getTurn() == 2:
        b.play(bot.play(b.colNotFull()))
    if b.checkWin():
        print('player %i won' % b.turn)
        b.restart()
    else:
        print('player %i played' % b.turn)
        b.changeTurn()
