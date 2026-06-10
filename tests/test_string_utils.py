import string_utils

def test_reverse_string():
    assert string_utils.reverse_string("abc") == "cba"
    assert string_utils.reverse_string("") == ""

