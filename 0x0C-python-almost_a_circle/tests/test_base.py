#!/usr/bin/python3
"""Base class test cases"""


import unittest
from models.base import Base

class testBase(unittest.TestCase):
    """test cases for Base class"""

    def test_id_increment(self):
        """tests id increment"""
        t_1 = Base()
        t_2 = Base()

        self.assertGreater(t_2.id, 0)
