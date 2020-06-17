import ActivationFunctions

global geneIndex
geneIndex = 0


class __Gene():
    index: int = None
    enabled: bool = True


class Connect(__Gene):
    start: int = None
    end: int = None
    weight: float = 1
    bias: float = 0.0

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

    def value(self, value: float):
        return (value * self.weight) + self.bias


class Node(__Gene):
    nodeType: str = None
