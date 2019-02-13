from random import randint


class DumbBot():
    def __init__(self):
        pass

    def play(self, colList):
        return randint(0, len(colList) - 1)
