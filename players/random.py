from random import choice


class RandomPlayer:
    # this class will play a random valid move

    def __init__(self):
        pass

    def play(self, state):
        possible_moves = []
        for col in range(7):
            if state[0][col] == 0:
                possible_moves.append(col)

        return choice(possible_moves)