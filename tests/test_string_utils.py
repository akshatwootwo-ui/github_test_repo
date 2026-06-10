import unittest
import string_utils

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string("hello"), "olleh")
