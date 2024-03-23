import unittest
from matemathic_function.is_triangle import is_triangle


class TestIsTriangle(unittest.TestCase):

    def test_is_triangle_true(self):
        # Given
        side1 = 5
        side2 = 8
        side3 = 10
        # When
        result = is_triangle(side1, side2, side3)
        # Then
        self.assertEqual(result, True)

    def test_is_triangle_false(self):
        # Given
        side1 = 5
        side2 = 10
        side3 = 20
        # When
        result = is_triangle(side1, side2, side3)
        # Then
        self.assertEqual(result, False)

    def test_is_triangle_negative_side(self):
        # Given
        side1 = -5
        side2 = 5
        side3 = 4
        # When
        result = is_triangle(side1, side2, side3)
        # Then
        self.assertEqual(result, False)
