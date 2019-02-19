import os

from game.game import Board

from players.human import HumanPlayer
from players.random import RandomPlayer
from players.minimax import MinimaxPlayer


def main():

    # clear terminal
    os.system("clear")

    # print game info
    print()
    print("   --------------------------------")
    print("   |                              |")
    print("   |   CONNECT 4 - UAIS PROJECT   |")
    print("   |                              |")
    print("   --------------------------------")

    # get player 1
    print()
    print("   Select player 1 type:")
    print("   1. Human")
    print("   2. Random")
    print("   3. Minimax")

    choice = input()
    while choice not in ("1", "2", "3"):
        print("  invalid input, please try again")
        choice = input()

    if choice == "1":
        player1 = HumanPlayer()
    elif choice == "2":
        player1 = RandomPlayer()
    elif choice == "3":
        player1 = MinimaxPlayer()

    # get player 2
    print()
    print("   Select player 2 type:")
    print("   1. Human")
    print("   2. Random")
    print("   3. Minimax")

    choice = input()
    while choice not in ("1", "2", "3"):
        print("  invalid input, please try again")
        choice = input()

    if choice == "1":
        player2 = HumanPlayer()
    elif choice == "2":
        player2 = RandomPlayer()
    elif choice == "3":
        player2 = MinimaxPlayer()

    board = Board(player1, player2)

    playAgain = "Y"
    while playAgain == "Y":

        # this actually plays the game
        board.playGame()

        print("   Play again? (Y/N)")
        playAgain = input().upper()
        while playAgain not in ("Y", "N"):
            playAgain = input().upper()

if __name__ == "__main__":
    main()