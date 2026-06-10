import unittest
import string_utils

class TestString_utils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string("hello"), "olleh")
        self.assertEqual(string_utils.reverse_string(""), "")
        self.assertEqual(string_utils.reverse_string("a"), "a")
