#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_ordered_list(self):
        """Test a list in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the maximum value is at the beginning."""
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)

    def test_max_at_end(self):
        """Test when the maximum value is at the end."""
        self.assertEqual(max_integer([1, 2, 5, 10]), 10)

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test calling max_integer with no arguments."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_mixed_positive_and_negative(self):
        """Test a list containing both negative and positive integers."""
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    def test_duplicate_max_values(self):
        """Test a list where the maximum value appears multiple times."""
        self.assertEqual(max_integer([4, 2, 4, 1, 4]), 4)

    def test_all_same_values(self):
        """Test a list where all elements are identical."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_floats(self):
        """Test a list of floats and mixed ints/floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")
        self.assertEqual(max_integer(["abc", "abd"]), "abd")

    def test_empty_string_in_list(self):
        """Test a list containing an empty string."""
        self.assertEqual(max_integer(["", "a"]), "a")

    def test_none_argument_raises_type_error(self):
        """Test passing None raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable_raises_type_error(self):
        """Test passing a non-iterable raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(123)

    def test_incomparable_types_raises_type_error(self):
        """Test comparing incompatible types raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


if __name__ == '__main__':
    unittest.main()
