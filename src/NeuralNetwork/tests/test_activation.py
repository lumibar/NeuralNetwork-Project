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

    @params((1, 0.79), (2, 1.11), (3, 1.25), (4.5, 1.35), (102, 1.56), (-1, -0.79), (-23.4, -1.53))
    def testArcTan(self, x, y):
        self.assertAlmostEqual(ActivationFunctions.arcTan(x), y, 2)

    @params((1, 0.88), (2, 1.44), (3, 1.82), (4.5, 2.21), (102, 5.32), (-1, -0.88), (-23.4, -3.85))
    def testArcSinH(self, x, y):
        self.assertAlmostEqual(ActivationFunctions.arcSinH(x), y, 2)

    @params((1, 0.5), (2, 0.67), (3, 0.75), (4.5, 0.82), (102, 0.99), (-1, -0.5), (-23.4, -0.96))
    def testElliotSig(self, x, y):
        self.assertAlmostEqual(ActivationFunctions.elliotSig(x), y, 2)

    @params((1, 0.71), (2, 0.89), (3, 0.95), (4.5, 0.98), (102, 1), (-1, -0.71), (-23.4, -1))
    def testInverseSquareRoot(self, x, y):
        self.assertAlmostEqual(ActivationFunctions.inverseSquareRoot(x), y, 2)

    @params((1, 1), (2, 2), (3, 3), (4.5, 4.5), (102, 102), (-1, 0), (-23.4, 0))
    def testRectifiedLinear(self, x, y):
        self.assertEqual(ActivationFunctions.rectifiedLinear(x), y)

    @params((1, 0), (2, 2), (3, 0), (4.5, 0), (102, 102), (-1, -1), (-23.4, -23.4))
    def testBipolarRectifiedLinear(self, x, y):
        self.assertEqual(ActivationFunctions.bipolarRectifiedLinear(x), y)

    @params((1, 1), (2, 2), (3, 3), (4.5, 4.5), (102, 102), (-1, -0.001), (-23.4, -0.234))
    def testLeakyRectifiedLinear(self, x, y):
        self.assertEqual(ActivationFunctions.leakyRectifiedLinear(x), y)

    @params((1, 1), (2, 2), (3, 3), (4.5, 4.5), (102, 102), (-1, -0.5), (-23.4, -11.7))
    def testParametricRectifiedLinear(self, x, y):
        self.assertEqual(ActivationFunctions.parametricRectifiedLinear(x), y)

    @params((1, 1), (2, 2), (3, 3), (4.5, 4.5), (102, 102), (-1, -0.63), (-23.4, -1))
    def testExponentialLinear(self, x, y):
        self.assertAlmostEqual(ActivationFunctions.exponentialLinear(x), y, 2)

    @params((1, 1), (2, 2), (3, 3), (4.5, 4.5), (102, 102), (-1, -0.66), (-23.4, -1.05))
    def testScaledExponentialLinear(self, x, y):
        self.assertAlmostEqual(
            ActivationFunctions.scaledExponentialLinear(x), y, 2)
