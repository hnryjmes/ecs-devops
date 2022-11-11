"""Unit test file for app.py"""
from app import return_backwards_string
import unittest


class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""

    def test_return_backwards_string(self):
        """Test return backwards simple string"""
        the_string = "This is my test string"
        the_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(the_string_reversed, return_backwards_string(the_string))


if __name__ == "__main__":
    unittest.main()
