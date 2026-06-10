import unittest
import string_utils

class TestString_utils(unittest.TestCase):
    # Add test cases here
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string("abc"), "cba")
        self.assertEqual(string_utils.reverse_string(""), "")
