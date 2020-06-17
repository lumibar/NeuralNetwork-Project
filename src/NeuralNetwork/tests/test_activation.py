import unittest
from nose2.tools import params
from NeuralNetwork import ActivationFunctions

# A series of tests for the activation functions
# Parameters are x as the input and y as expected outcome


class ActivationTest(unittest.TestCase):
    @params((1, 1), (2, 2), (3, 3), (4.5, 4.5), (102, 102), (-1, -1), (-23.4, -23.4))
    def testIdentity(self, x, y):
        self.assertEqual(ActivationFunctions.identity(x), y)

    @params((1, 1), (2, 1), (3, 1), (4.5, 1), (102, 1), (-1, 0), (-23.4, 0))
    def testBinaryStep(self, x, y):
        self.assertEqual(ActivationFunctions.binaryStep(x), y)

    @params((1, 0.73), (2, 0.88), (3, 0.95), (4.5, 0.99), (102, 1), (-1, 0.27), (-23.4, 0))
    def testSigmoid(self, x, y):
        self.assertAlmostEqual(ActivationFunctions.sigmoid(x), y, 2)

    @params((1, 0.76), (2, 0.96), (3, 1), (4.5, 1), (102, 1), (-1, -0.76), (-23.4, -1))
    def testTanh(self, x, y):
        self.assertAlmostEqual(ActivationFunctions.tanH(x), y, 2)

    @params((1, 0.75), (2, 1), (3, 1), (4.5, 1), (102, 1), (-1, -0.75), (-23.4, -1))
    def testSQNL(self, x, y):
        self.assertEqual(ActivationFunctions.sqnl(x), y)
