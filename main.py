from game.game import Board

from players.human import HumanPlayer
from players.random import RandomPlayer
from players.minimax import MinimaxPlayer


def main():
    # print game info
    print()
    print("   --------------------------------")
    print("   |                              |")
    print("   |   CONNECT 4 - UAIS PROJECT   |")
    print("   |                              |")
    print("   --------------------------------")

    # get players
    print()
    print("   Select player 1 type:")
    print("   1. Human")
    print("   2. Random")
    print("   3. Minimax")

    choice = input()
    while choice not in ("1", "2", "3"):
        choice = input()
    if choice == "1":
        player1 = HumanPlayer()
    elif choice == "2":
        player1 = RandomPlayer()
    elif choice == "3":
        player1 = MinimaxPlayer()

    print()
    print("   Select player 2 type:")
    print("   1. Human")
    print("   2. Random")
    print("   3. Minimax")

    choice = input()
    while choice not in ("1", "2", "3"):
        choice = input()
    if choice == "1":
        player2 = HumanPlayer()
    elif choice == "2":
        player2 = RandomPlayer()
    elif choice == "3":
        player2 = MinimaxPlayer()

    board = Board(player1, player2)

    board.playGame()

if __name__ == "__main__":
    main()