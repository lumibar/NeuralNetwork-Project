from NeuralNetwork import ActivationFunctions

global geneIndex
geneIndex = 0


class _Gene():
    index: int
    enabled: bool


class Connect(_Gene):
    weight: float
    bias: float

    def __init__(self, start: int, stop: int, enabled: bool = True, weight: float = None):
        super().__init__()
        global geneIndex
        self.index = geneIndex
        geneIndex += 1
        self.start = start
        self.end = stop
        self.enabled = enabled
        if weight:
            self.weight = weight

    def value(self, value):
        return (value * self.weight) + self.bias


class Node(_Gene):
    nodeType: str = None
