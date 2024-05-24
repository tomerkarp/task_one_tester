import unittest
from unittest.mock import patch
from io import StringIO
import os

class TestMainProgram(unittest.TestCase):
    # =============================================================================================================
    # TODO: Set the file name here to match your main Python file (Task_1, 'main.py')
    file_name = 'Task_one.py'  # TODO:<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # =============================================================================================================
    # =============================================================================================================
    f_n = os.path.join(os.path.dirname(__file__), file_name)
    def run_code_with_input(self, inputs):
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                try:
                    with open(self.f_n, encoding='utf-8') as f:
                        code = f.read()
                        exec(code, globals())
                except SystemExit:
                    pass

                return mock_stdout.getvalue()

    # Test cases for Exercise 1
    def test_exercise_1_valid_leap_year(self):
        output = self.run_code_with_input(['1', '29', '2', '2020'])
        self.assertIn("The date is valid.", output)

    def test_exercise_1_invalid_non_leap_year(self):
        output = self.run_code_with_input(['1', '30', '2', '2021'])
        self.assertIn("Invalid date.", output)

    def test_exercise_1_invalid_date(self):
        output = self.run_code_with_input(['1', '31', '4', '2021'])
        self.assertIn("Invalid date.", output)

    # Test cases for Exercise 3
    def test_exercise_3_prime_number(self):
        output = self.run_code_with_input(['3', '10'])
        self.assertIn("The first prime number greater than 10 is: 11", output)

    def test_exercise_3_next_sorted_number_from_prime(self):
        output = self.run_code_with_input(['3', '123'])
        self.assertIn("The first prime number greater than 123 is: 127", output)
        self.assertIn("The first number with digits in ascending order as a List is: [1, 2, 8]", output)

    def test_exercise_3_prime_and_sorted(self):
        output = self.run_code_with_input(['3', '20'])
        self.assertIn("The first prime number greater than 20 is: 23", output)
        self.assertIn("The first number with digits in ascending order as a List is: [2, 4]", output)

    # Test cases for Exercise 4
    def test_exercise_4_scalene_right_triangle(self):
        output = self.run_code_with_input(['4', '3 4 5'])
        self.assertIn("('Scalene', 'Right')", output)

    def test_exercise_4_equilateral_triangle(self):
        output = self.run_code_with_input(['4', '5 5 5'])
        self.assertIn("('Equilateral', 'Acute')", output)

    def test_exercise_4_illegal_triangle(self):
        output = self.run_code_with_input(['4', '1 1 3'])
        self.assertIn("Illegal triangle", output)

    # Test cases for Exercise 4
    def test_exercise_4_scalene_right_triangle2(self):
        output = self.run_code_with_input(['4', '3 4 5'])
        self.assertIn("('Scalene', 'Right')", output)

    def test_exercise_4_equilateral_triangle2(self):
        output = self.run_code_with_input(['4', '5 5 5'])
        self.assertIn("('Equilateral', 'Acute')", output)

    def test_exercise_4_illegal_triangle2(self):
        output = self.run_code_with_input(['4', '1 1 3'])
        self.assertIn("Illegal triangle", output)

    def test_exercise_4_isosceles_acute_triangle(self):
        output = self.run_code_with_input(['4', '5 5 8'])
        self.assertIn("('Isosceles', 'Obtuse')", output)

    def test_exercise_4_scalene_acute_triangle(self):
        output = self.run_code_with_input(['4', '6 8 10'])
        self.assertIn("('Scalene', 'Right')", output)

    def test_exercise_4_scalene_acute_triangle_flipped(self):
        output = self.run_code_with_input(['4', '10 8 6'])
        self.assertIn("('Scalene', 'Right')", output)

    def test_exercise_4_isosceles_obtuse_triangle(self):
        output = self.run_code_with_input(['4', '5 5 9'])
        self.assertIn("('Isosceles', 'Obtuse')", output)

    def test_exercise_4_scalene_obtuse_triangle(self):
        output = self.run_code_with_input(['4', '7 9 12'])
        self.assertIn("('Scalene', 'Obtuse')", output)

    def test_exercise_4_scalene_obtuse_triangle_flipped(self):
        output = self.run_code_with_input(['4', '12 7 9'])
        self.assertIn("('Scalene', 'Obtuse')", output)

    def test_exercise_4_large_scalene_triangle(self):
        output = self.run_code_with_input(['4', '50 70 100'])
        self.assertIn("('Scalene', 'Obtuse')", output)

    def test_exercise_4_illegal_triangle_zero_side(self):
        output = self.run_code_with_input(['4', '0 5 5'])
        self.assertIn("Illegal triangle", output)

    def test_exercise_4_valid_small_triangle(self):
        output = self.run_code_with_input(['4', '1 1 1'])
        self.assertIn("('Equilateral', 'Acute')", output)

    # Test cases for Exercise 3
    def test_exercise_3_prime_number2(self):
        output = self.run_code_with_input(['3', '10'])
        self.assertIn("The first prime number greater than 10 is: 11", output)

    def test_exercise_3_next_sorted_number_from_prime2(self):
        output = self.run_code_with_input(['3', '123'])
        self.assertIn("The first prime number greater than 123 is: 127", output)
        self.assertIn("The first number with digits in ascending order as a List is: [1, 2, 8]", output)

    def test_exercise_3_prime_and_sorted2(self):
        output = self.run_code_with_input(['3', '20'])
        self.assertIn("The first prime number greater than 20 is: 23", output)
        self.assertIn("The first number with digits in ascending order as a List is: [2, 4]", output)

    def test_exercise_3_large_number(self):
        output = self.run_code_with_input(['3', '1000'])
        self.assertIn("The first prime number greater than 1000 is: 1009", output)
        self.assertIn("The first number with digits in ascending order as a List is: [1, 2, 3, 4]", output)

    def test_exercise_3_edge_prime(self):
        output = self.run_code_with_input(['3', '29'])
        self.assertIn("The first prime number greater than 29 is: 31", output)
        self.assertIn("The first number with digits in ascending order as a List is: [3, 4]", output)

    def test_exercise_3_prime_less_than_10(self):
        output = self.run_code_with_input(['3', '7'])
        self.assertIn("The first prime number greater than 7 is: 11", output)
        self.assertIn("The first number with digits in ascending order as a List is: [1, 2]", output)

    def test_exercise_3_high_prime(self):
        output = self.run_code_with_input(['3', '200'])
        self.assertIn("The first prime number greater than 200 is: 211", output)
        self.assertIn("The first number with digits in ascending order as a List is: [2, 3, 4]", output)

    def test_exercise_3_prime_ending_with_7(self):
        output = self.run_code_with_input(['3', '97'])
        self.assertIn("The first prime number greater than 97 is: 101", output)
        self.assertIn("The first number with digits in ascending order as a List is: [1, 2, 3]", output)

    def test_exercise_3_large_prime(self):
        output = self.run_code_with_input(['3', '300'])
        self.assertIn("The first prime number greater than 300 is: 307", output)
        self.assertIn("The first number with digits in ascending order as a List is: [3, 4, 5]", output)

    def test_exercise_3_prime_closer_to_1000(self):
        output = self.run_code_with_input(['3', '950'])
        self.assertIn("The first prime number greater than 950 is: 953", output)
        self.assertIn("The first number with digits in ascending order as a List is: [1, 2, 3, 4]", output)

    # Test cases for Exercise 1
    def test_exercise_1_valid_leap_year2(self):
        output = self.run_code_with_input(['1', '29', '2', '2020'])
        self.assertIn("The date is valid.", output)

    def test_exercise_1_invalid_non_leap_year2(self):
        output = self.run_code_with_input(['1', '30', '2', '2021'])
        self.assertIn("Invalid date.", output)

    def test_exercise_1_invalid_date2(self):
        output = self.run_code_with_input(['1', '31', '4', '2021'])
        self.assertIn("Invalid date.", output)

    def test_exercise_1_valid_regular_year(self):
        output = self.run_code_with_input(['1', '15', '7', '2021'])
        self.assertIn("The date is valid.", output)

    def test_exercise_1_invalid_day(self):
        output = self.run_code_with_input(['1', '32', '1', '2021'])
        self.assertIn("Invalid date.", output)

    def test_exercise_1_invalid_month(self):
        output = self.run_code_with_input(['1', '15', '13', '2021'])
        self.assertIn("Invalid date.", output)

    def test_exercise_1_valid_date_end_of_month(self):
        output = self.run_code_with_input(['1', '31', '12', '2021'])
        self.assertIn("The date is valid.", output)

    def test_exercise_1_invalid_date_feb_non_leap(self):
        output = self.run_code_with_input(['1', '29', '2', '2019'])
        self.assertIn("Invalid date.", output)

    def test_exercise_1_valid_date_feb_non_leap(self):
        output = self.run_code_with_input(['1', '28', '2', '2019'])
        self.assertIn("The date is valid.", output)

    def test_exercise_1_valid_ancient_year(self):
        output = self.run_code_with_input(['1', '15', '7', '150'])
        self.assertIn("The date is valid.", output)

    def test_exercise_1_valid_year_boundary(self):
        output = self.run_code_with_input(['1', '1', '1', '2100'])
        self.assertIn("The date is valid.", output)


# Run the test cases
if __name__ == "__main__":
    unittest.main()
