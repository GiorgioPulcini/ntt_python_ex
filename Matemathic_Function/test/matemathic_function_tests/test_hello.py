import unittest
from matemathic_function.hello import hello


class HelloTest(unittest.TestCase):
    def test_hello(self):
        # Given
        given_str = "Hello friend"
        given_name = "friend"
        # When
        test_str = hello(given_name)
        # Then
        self.assertEqual(given_str, test_str)
