from random import randint


class DumbBot():
    def __init__(self):
        pass

    def play(self, colList):
        # chooses a random column to play from the choices given
        return randint(0, len(colList) - 1)
