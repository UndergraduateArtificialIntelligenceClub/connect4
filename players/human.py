class HumanPlayer:
    def __init__(self):
        pass

    def play(self, state):
        print("Enter your move:")
        while True:
            choice = input()
            if choice in ("1", "2", "3", "4", "5", "6", "7") and state[0][int(choice) - 1] == 0:
                return int(choice) - 1