import calculator
import unittest

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calculator.add(2, 3), 5)

  def test_multiply(self):
    self.assertEqual(calculator.multiply(2, 3), 6)
