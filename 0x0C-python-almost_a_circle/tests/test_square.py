#!/usr/bin/python3
"""Square class tests"""

import unittest
from models.square import Square
from models.base import Base

class testSquare(unittest.TestCase):
    """Square tests"""

    def test_side(self):
        sq = Square(10)
        self.assertEqual(sq.side, 10)

    def test_update_args(self):
        sq = Square(10, 20, 30, 40)
        self.assertEqual([sq.size, sq.x, sq.y, sq.id], [10, 20, 30, 40])
        sq.update(4, 2, 3, 1)
        self.assertEqual([sq.id, sq.size, sq.x, sq.y], [4, 2, 3, 1])

    def test_update_kwargs(self):
        sq = Square(1, 1, 1, 1)
        sq.update(size=10, x=20, y=30, id=40)
        self.assertEqual([sq.size, sq.x, sq.y, sq.id], [10, 20, 30, 40])

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
