import unittest
from math_functions import is_even
from math_functions import sum_function
from math_functions import sub_function
from math_functions import mul_function
from math_functions import div_function2
from math_functions import modulo_func
from math_functions import is_odd


class TestMathFunctions(unittest.TestCase):

    def test_modulo_true(self):
        number1 = 0
        number2 = -2
        number3 = 2
        result1 = modulo_func(number1)
        result2 = modulo_func(number2)
        result3 = modulo_func(number3)
        self.assertEqual(result1, 0, "answer is correct ")
        self.assertEqual(result2, 0, "answer is correct ")
        self.assertEqual(result3, 0, "answer is correct ")

    def test_modulo_false(self):
        number1 = 3
        number2 = -3
        result1 = modulo_func(number1)
        result2 = modulo_func(number2)
        self.assertNotEqual(result1, 0, "answer is correct ")
        self.assertNotEqual(result2, 0, "answer is correct ")

    def test_is_odd_true(self):
        number1 = 3
        number2 = -3
        result1 = is_odd(number1)
        result2 = is_odd(number2)
        self.assertNotEqual(result1, 0, "correct the answer is not 0")
        self.assertNotEqual(result2, 0, "correct the answer is not 0")

    def test_is_even_true(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))

    def test_is_even_false(self):
        self.assertFalse(is_even(5))
        self.assertFalse(is_even(-5))

    def test_sum_function_is_correct(self):
        number = 5
        result1 = sum_function(2, 3)
        result2 = sum_function(0, 5)
        result3 = sum_function(-1, 6)
        self.assertEqual(number, result1, "sum of two number is 5 - result is true")
        self.assertEqual(number, result2, "sum of two number is 5 - result is true")
        self.assertEqual(number, result3, "sum of two number is 5 - result is true")

    def test_sum_function_not_correct(self):
        number = 6
        result1 = sum_function(2, 3)
        result2 = sum_function(0, 3)
        result3 = sum_function(-1, 3)
        self.assertEqual(number, result1, "sum of two numbers is not 5 - result is false")
        self.assertEqual(number, result2, "sum of two numbers is not 5 - result is false")
        self.assertEqual(number, result3, "sum of two numbers is not 5 - result is false")

    def test_sub_function_is_correct(self):
        number = 1
        result1 = sub_function(3, 2)
        result2 = sub_function(-1, -2)
        result3 = sub_function(1, 0)
        self.assertEqual(number, result1, "total sub is correct")
        self.assertEqual(number, result2, "total sub is correct")
        self.assertEqual(number, result3, "total sub is correct")

    def test_sub_function_is_not_correct(self):
        number = 1
        result1 = sub_function(3, 1)
        result2 = sub_function(3, 0)
        result3 = sub_function(-1, 2)
        result4 = sub_function(-2, 1)
        result5 = sub_function(-2, -2)
        self.assertEqual(number, result1, "total sub is not correct")
        self.assertEqual(number, result2, "total sub is not correct")
        self.assertEqual(number, result3, "total sub is not correct")
        self.assertEqual(number, result4, "total sub is not correct")
        self.assertEqual(number, result5, "total sub is not correct")

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
        result1 = div_function2(10, 5)
        result2 = div_function2(-10, -5)
        self.assertEqual(number, result1, "total division is correct")
        self.assertEqual(number, result2, "total division is correct")

    def test_div_function_not_correct(self):
        number = 2
        result1 = div_function2(11, 5)
        result2 = div_function2(-11, -5)
        self.assertNotEqual(number, result1, "correct total division is not 2")
        self.assertNotEqual(number, result2, "correct total division is not 2")
        with self.assertRaises(TypeError):
            div_function2(10, 0)
            div_function2(-10, 0)
            div_function2(0, 0)



if __name__ == '__main__':
    unittest.main()
