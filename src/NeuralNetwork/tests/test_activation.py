import unittest


class ActivationTest(unittest.TestCase):
    def testIdentity(self):
        import ActivationFunctions
        self.assertEqual(ActivationFunctions.identity(1), 1)
