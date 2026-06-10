import calculator
import unittest

def test_add():
  assert calculator.add(2, 3) == 5

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
