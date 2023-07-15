import unittest

from grazincalculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test all functions from calculator module"""

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3.3, 2.1, 1.05)
        self.assertEqual(result, 6.45)
        result = self.calculator.add(1)
        self.assertEqual(result, 7.45)

    def test_subtract(self):
        result = self.calculator.subtract(0.3, 0.1)
        self.assertEqual(result, 0.2)
        result = self.calculator.subtract(1.2)
        self.assertEqual(result, -1)

    def test_multiply(self):
        result = self.calculator.multiply(0.1, 0.2)
        self.assertEqual(result, 0.02)
        result = self.calculator.multiply(3)
        self.assertEqual(result, 0.06)

    def test_divide(self):
        result = self.calculator.divide(10, 2.5, 1.25)
        self.assertEqual(result, 3.2)
        result = self.calculator.divide(2)
        self.assertEqual(result, 1.6)

    def test_root(self):
        result = self.calculator.root(8, 3)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
