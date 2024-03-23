import unittest
from Matemathic_Function.src.matemathic_function.math_function import EquilateralTriangle, IsoscelesTriangle, \
    ScaleneTriangle


class TriangleTest(unittest.TestCase):

    def test_equilateral_triangle(self):
        # Given
        given_side = 6
        given_perimeter = 18.0
        given_area = 15.588
        # When
        test_et = EquilateralTriangle(given_side)
        # Then
        self.assertEqual(given_perimeter, test_et.perimeter())
        self.assertEqual(given_area, test_et.area())

    def test_isosceles_triangle(self):
        # Given
        given_base_side = 6
        given_lateral_side = 8.0
        given_perimeter = 22.0
        given_area = 22.249
        # When
        test_it = IsoscelesTriangle(given_base_side, given_lateral_side)
        # Then
        self.assertEqual(given_perimeter, test_it.perimeter())
        self.assertEqual(given_area, test_it.area())

    def test_scalene_triangle(self):
        # Given
        given_side1 = 6
        given_side2 = 8
        given_side3 = 10
        given_perimeter = 24.0
        given_area = 24.0
        # When
        test_st = ScaleneTriangle(given_side1, given_side2, given_side3)
        # Then
        self.assertEqual(given_perimeter, test_st.perimeter())
        self.assertEqual(given_area, test_st.area())
