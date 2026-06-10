import string_utils
import unittest

def test_to_upper():
  assert string_utils.to_upper("hello") == "HELLO"

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string("hello"), "olleh")
