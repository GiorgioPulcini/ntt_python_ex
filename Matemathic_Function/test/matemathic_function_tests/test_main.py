import unittest
from unittest.mock import patch
from io import StringIO
from Matemathic_Function.src.matemathic_function.main import main


class TestMain(unittest.TestCase):

    @patch("builtins.input", side_effect=["Giorgio", "Equilateral", 3])
    @patch('sys.stdout', new_callable=StringIO)
    def test_equilateral_triangle_all_right(self, mock_stdout, mock_input):
        main()
        self.assertIn("Perimeter: 9.0", mock_stdout.getvalue())
        self.assertIn("Area: 3.897", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["Giorgio", "Isosceles", 5, 10])
    @patch('sys.stdout', new_callable=StringIO)
    def test_isosceles_triangle_all_right(self, mock_stdout, mock_input):
        main()
        self.assertIn("Perimeter: 25.0", mock_stdout.getvalue())
        self.assertIn("Area: 24.206", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["Giorgio", "Scalene", 5, 10, 12])
    @patch('sys.stdout', new_callable=StringIO)
    def test_scalene_triangle_all_right(self, mock_stdout, mock_input):
        main()
        self.assertIn("Perimeter: 27.0", mock_stdout.getvalue())
        self.assertIn("Area: 24.545", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["Giorgio", "not_valid_triangle_type"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_not_valid_triangle_type(self, mock_stdout, mock_input):
        main()
        self.assertIn("Sorry, I don't understand", mock_stdout.getvalue())
