#!/usr/bin/python3
"""tests for max integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([12]), 12)
        self.assertEqual(max_integer([23, -1, -5, 0]), 23)
        self.assertEqual(max_integer([-1, -2, -4, -9]), -1)
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    # def test_raises(self):
    #     self.assertRaises(ValueError, max_integer, "max")
    #     self.assertRaises(ValueError, max_integer, 1)
    #     self.assertRaises(ValueError, max_integer, 12.0)
    #     self.assertRaises(ValueError, max_integer, (1, 3, 4))
