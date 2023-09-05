#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([..])"""

    def test_ordered_list(self):
        """Test an ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        unordered = [2, 4, 1, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_from_max(self):
        """Test list from max at beginning"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test only one element"""
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

    def test_floats(self):
        """Test list of floats"""
        list_floats = [1.2, 3.4, 7.1, 23.5]
        self.assertEqual(max_integer(list_floats), 23.5)

    def test_ints_and_floats(self):
        """Test list of ints and floats"""
        int_and_float = [7, 23.4, 34, 92.4]
        self.assertEqual(max_integer(int_and_float), 92.4)

    def test_string(self):
        """Test one string"""
        string = "Who"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test list of strings"""
        strings = ["Who", "am", "i", "?"]
        self.assertEqual(max_integer(strings), "i")

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
