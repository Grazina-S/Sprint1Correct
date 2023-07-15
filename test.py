import unittest

from grazincalculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test all functions from calculator module"""

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3.3, 2.1, 21.05)
        self.assertAlmostEqual(result, 26.45, places=6)

    def test_substract(self):
        result = self.calculator.substract(0.3, 0.1)
        self.assertAlmostEqual(result, 0.2, places=6)

    def test_multiply(self):
        result = self.calculator.multiply(0.1, 0.2)
        self.assertAlmostEqual(result, 0.02, places=6)

    def test_divide(self):
        result = self.calculator.divide(10, 2.5, 1.2)
        self.assertAlmostEqual(result, 3.333333, places=6)

    def test_root(self):
        result = self.calculator.root(7, 2)
        self.assertAlmostEqual(result, 2.645751, places=6)


if __name__ == "__main__":
    unittest.main()