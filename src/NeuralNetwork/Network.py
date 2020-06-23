from NeuralNetwork import Genes


class Network():

    def __init__(self, inputNodes: list, outputNodes: list):
        self.nextNodeIndex = 0
        self.nextInputIndex = 0
        self.connectGenes = []
        self.nodeGenes = []
        self.calculated = {}

        for node in inputNodes:
            self.nodeGenes.append(Genes.Node(
                self.nextNodeIndex, "input", inputIndex=self.nextInputIndex))
            self.nextNodeIndex += 1
            self.nextInputIndex += 1
        for node in outputNodes:
            self.nodeGenes.append(Genes.Node(
                self.nextNodeIndex, "output", "sigmoid"))
            self.nextNodeIndex += 1
