from datetime import datetime


class MinimaxPlayer:
    # this class uses minmax algorithm to play the game 100% optimally
    # as of 16/02/2019, the minimax function runs ~1000s of times per second 
    # it is not nearly fast enough for real play, with billions of possible states at the start of the game


    def __init__(self):
        
        self.trackTime = True
        if self.trackTime:
            self.count = 0
            self.time = datetime.now()

        self.possible_wins = [
            # horizontal
            [0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6],[7,8,9,10],[8,9,10,11],[9,10,11,12],[10,11,12,13],
            [14,15,16,17],[15,16,17,18],[16,17,18,19],[17,18,19,20],[21,22,23,24],[22,23,24,25],[23,24,25,26],[24,25,26,27],
            [28,29,30,31],[29,30,31,32],[30,31,32,33],[31,32,33,34],[35,36,37,38],[36,37,38,39],[37,38,39,40],[38,39,40,41],
            # vertical
            [0,7,14,21],[7,14,21,28],[14,21,28,35],[1,8,15,22],[8,15,22,29],[15,22,29,36],[2,9,16,23],
            [9,16,23,30],[16,23,30,37],[3,10,17,24],[10,17,24,31],[17,24,31,38],[4,11,18,25],[11,18,25,32],
            [18,25,32,39],[5,12,19,26],[12,19,26,33],[19,26,33,40],[6,13,20,27],[13,20,27,34],[20,27,34,41],
            # top-left to bottom-right diagonal
            [0,8,16,24],[1,9,17,25],[2,10,18,26],[3,11,19,27],[7,15,23,31],[8,16,24,32],
            [9,17,25,33],[10,18,26,34],[14,22,30,38],[15,23,31,39],[16,24,32,40],[17,25,33,41],
            # bottom-left to top-right diagonal
            [21,15,9,3],[22,16,10,4],[23,17,11,5],[24,18,12,6],[28,22,16,10],[29,23,17,11],
            [30,24,18,12],[31,25,19,13],[35,29,23,17],[36,30,24,18],[37,31,25,19],[38,32,26,20]
        ]

    def play(self, state):
        
        if self.trackTime:
            self.count = 0
            self.time = datetime.now()

        depth = 0
        maxLevel = 1
        num_ones = 0
        num_twos = 0

        flattened = []

        for row in state:
            for cell in row:
                flattened.append(cell)
                if cell == 1:
                    num_ones += 1
                    depth += 1
                elif cell == 2:
                    num_twos += 1
                    depth += 1
        
        depth = num_ones + num_twos

        if num_ones > num_twos:
            self.player = 2
        elif num_ones == num_twos:
            self.player = 1

        # returns the best play returned by the Minimax algorithm
        return self.minimax(flattened, 0, maxLevel, self.player, True)[0]

    def minimax(self, state, depth, maxLevel, turn, first_call):
        print('depth:', depth)
        if depth == maxLevel:
            result = self.checkWin(state)
            if result in (1, 2):
                return 1
            else:
                return 0
        moves = []
        for move in self.getPossibleMoves(state):
            new_state = self.getNewState(state, move, turn)
            moves.append((move, self.minimax(new_state, depth + 1, maxLevel, 3 - turn, first_call)))
        print('max move:', max(moves, key=lambda x:x[1]))
        return max(moves, key=lambda x:x[1])

    def calculateScore(self, result, depth):
        if result == self.player:
            return 100 - depth
        elif result == 0:
            return depth
        else:
            return depth - 100

    def checkWin(self, state):
        # checks for wins or draws
        # return values:
        # -1 = game not over
        # 0  = draw
        # 1  = player 1 win
        # 2  = player 2 win

        for win in self.possible_wins:
            if state[win[0]] != 0 and state[win[0]] == state[win[1]] == state[win[2]] == state[win[3]]:
                return state[win[0]]

        # check draw
        if 0 not in state[0:7]:
            return 0

        # no win or draw
        return -1

    def getPossibleMoves(self, state):
        # returns a list of all possible column index moves
        possible_moves = []
        for col in range(7):
            if state[col] == 0:
                possible_moves.append(col)
        return possible_moves

    def getNewState(self, state, move, turn):
        # makes a play and returns the new state
        pos = move + 35
        while pos >= 0:
            cell = state[pos]
            # if empty
            if cell == 0:
                state[pos] = turn
                return state
            else:
                pos -= 7