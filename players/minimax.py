from copy import deepcopy


class MinimaxPlayer():
    # bot that uses minmax algorithm to play
    def __init__(self, player):
        # to keep track how many times minimax function is called
        self.count = 0
        # variable to know which player bot is
        self.player = player

    def play(self, state, depth):
        # returns the best play returned by the Minimax algorithm
        return self.minimax(state, depth, self.player, True)

    def minimax(self, state, depth, turn, first_call):
        self.count += 1
        print(self.count)

        if self.gameOver(state):
            return self.calculateScore(state, depth)

        moves = self.getPossibleMoves(state)
        scores = []

        for move in moves:

            if self.gameOver(state):
                print("This shouldn't happen")

            new_state = self.getNewState(deepcopy(state), move, turn)

            score = self.minimax(new_state, depth + 1, 3 - turn, False)
            scores.append(score)

        if first_call:
            print(moves)
            print(scores)
            return moves[scores.index(max(scores))]

        if turn == self.player:
            return scores[scores.index(max(scores))]
        else:
            return scores[scores.index(min(scores))]

    def calculateScore(self, state, depth):
        if self.checkWinner(state, self.player):
            return 100 - depth
        elif self.checkWinner(state, 3 - self.player):
            return depth - 100
        else:
            return depth

    def checkWinner(self, state, player):
        for row in range(6):
            for col in range(4):
                if state[row][col] == state[row][col + 1] == state[row][col + 2] == state[row][col + 3] and state[row][col] == player:
                    return True

        for col in range(7):
            for row in range(3):
                if state[row][col] == state[row + 1][col] == state[row + 2][col] == state[row + 3][col] and state[row][col] == player:
                    return True

        for row in range(3):
            for col in range(4):
                if state[row][col] == state[row + 1][col + 1] == state[row + 2][col + 2] == state[row + 3][col + 3] and state[row][col] == player:
                    return True

        for row in range(3):
            for col in range(6, 2, -1):
                if state[row][col] == state[row + 1][col - 1] == state[row + 2][col - 2] == state[row + 3][col - 3] and state[row][col] == player:
                    return True

        return False

    def gameOver(self, state):
        # Check for a draw
        if 0 not in state[0]:
            return True

        # Check for player 1 win
        if self.checkWinner(state, 1):
            return True

        # Check for player 2 win
        if self.checkWinner(state, 2):
            return True

        return False

    def getPossibleMoves(self, state):
        # returns a list of all possible column index moves
        possible_moves = []
        for col in range(7):
            if state[0][col] == 0:
                possible_moves.append(col)
        return possible_moves

    def getNewState(self, state, move, turn):
        row = 5
        while row >= 0:
            cell = state[row][move]
            if cell == 0:
                state[row][move] = turn
                return state
            else:
                row -= 1


if __name__ == "__main__":
    state = [[0 for i in range(7)] for j in range(6)]
    minimax_player = Minimax(1)
    print(minimax_player.play(state, 0))
