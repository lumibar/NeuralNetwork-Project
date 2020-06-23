from NeuralNetwork import ActivationFunctions

global geneIndex
geneIndex = 0


def _dot(a, b):
    x = 0.0
    for i in range(len(a)):
        x += a[i]*b[i]
    return x


class _Gene():
    index: int
    enabled: bool


class Connect(_Gene):
    weight: float
    bias: float

    def __init__(self, start, stop, enabled=True, weight=0.0):
        global geneIndex
        self.index = geneIndex
        geneIndex += 1
        self.start = start
        self.end = stop
        self.enabled = enabled
        if weight:
            self.weight = weight

    def value(self, inputs, network):
        return network.nodeGenes[self.start].value()


class Node(_Gene):
    nodeType: str

    def __init__(self, index, nodeType: str = "hidden", activation=None, inputIndex=None):
        self.index = index
        self.nodeType = nodeType
        if self.nodeType == "input":
            self.inputIndex = inputIndex
        elif activation:
            self.activation = activation

    def value(self, inputs, network):
        if self.nodeType == "input":
            y = inputs[self.inputIndex]
            return getattr(ActivationFunctions, self.activation)(y)
        x = []
        for connect in network.connectGenes:
            if connect.end == self.index:
                if network.calcualted[connect.geneIndex]:
                    x[0].append(network.calcualted[connect.geneIndex])
                    x[1].append(connect.weight)
                else:
                    network.calcualted[connect.geneIndex] = connect.value(
                        inputs, network)
                    x[0].append(network.calcualted[connect.geneIndex])
                    x[1].append(connect.weight)
        y = _dot(x[0], x[1])
        return getattr(ActivationFunctions, self.activation)(y)
