import math

class NeuroNet():
    def __init__(self, layers):
        self.layers = []
        for l in layers:
            assert l % 1 == 0, "%d is not an integer" % l
            self.layers.append([0.0 for x in range(l)])


    def sum(self, layer):
        sum = 0.0
        for float in layer:
            sum += float
        return math.tanh(sum / 2)

n = NeuroNet([7, 2, 5])
print(n.sum(n.layers[0]))