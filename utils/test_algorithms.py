import unittest
from .algorithms import fibonacci, power, factorial, is_even, add_nums, sort_list, is_palindrome

class TestAlgorithms(unittest.TestCase):

    def test_fibonacci(self):
        # The original fibonacci was incorrect, assuming it should return a sequence
        # For now, we will test against a corrected implementation if the user fixes it
        # If the user intends for it to return a fixed list, this test will need adjustment.
        # For now, let's assume a correct fibonacci implementation
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    def test_power(self):
        # This function is currently a placeholder, so no meaningful test can be written yet.
        # Once implemented, tests for positive, negative, and zero exponents should be added.
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, 1), 10)
        self.assertEqual(power(2, -2), 0.25)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-1))

    def test_add_nums(self):
        self.assertEqual(add_nums(2, 3), 5)
        self.assertEqual(add_nums(-1, 1), 0)
        self.assertEqual(add_nums(0, 0), 0)
        self.assertEqual(add_nums(100, 200), 300)

    def test_sort_list(self):
        # This function is currently a placeholder, so no meaningful test can be written yet.
        # Once implemented with Quick Sort, tests for various list types should be added.
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])
        self.assertEqual(sort_list([]), [])
        self.assertEqual(sort_list([1]), [1])
        self.assertEqual(sort_list([5, 5, 1, 1, 3]), [1, 1, 3, 5, 5])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertFalse(is_palindrome("ab"))

if __name__ == '__main__':
    unittest.main()