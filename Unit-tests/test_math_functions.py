import unittest
from math_function import is_even
from math_function import sum_function
from math_function import sub_function
from math_function import mul_function
from math_function import div_function2


class TestMathFunctions(unittest.TestCase):

    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(5))

    def test_sum_function_is_correct(self):
        number = 5
        result = sum_function(2, 3)
        self.assertEqual(number, result, "sum of two number is 5 - result is true")

    def test_sum_function_not_correct(self):
        number = 6
        result = sum_function(2, 3)
        self.assertEqual(number, result, "sum of two numbers is not 5 - result is false")

    def test_sub_function_is_correct(self):
        number = 1
        result = sub_function(3, 2)
        self.assertEqual(number, result, "total sub is correct")

    def test_sub_function_is_not_correct(self):
        number = 1
        result = sub_function(3, 1)
        self.assertEqual(number, result, "total sub is not correct")

    def test_mul_function_is_correct(self):
        number = 10
        result = mul_function(2, 5)
        self.assertEqual(number, result, "total multiplication is correct")

    def test_mul_function_not_correct(self):
        number = 10
        result = mul_function(2, 6)
        self.assertEqual(number, result, "total multiplication is not correct")

    def test_div_function_is_correct(self):
        number = 2
        result = div_function2(10, 5)
        self.assertEqual(number, result, "total division is correct")

    def test_div_function_not_correct(self):
        with self.assertRaises(TypeError):
            div_function2(10, 0)


if __name__ == '__main__':
    unittest.main()
