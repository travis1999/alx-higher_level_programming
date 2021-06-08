#!/usr/bin/python3
"""Tests for the rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class rectangleTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rec = Rectangle(10, 10)

    def test_validate_int(self):
        self.assertRaises(TypeError, self.rec.validate_int, "sideT", [])

    def test_validate_dimension(self):
        self.assertRaises(TypeError, self.rec.validate_value, "sideT", "10")

    def test_validate_dimensionv(self):
        self.assertRaises(ValueError, self.rec.validate_value, "sideV", -100)

    def test_validate_position(self):
        self.assertRaises(TypeError, self.rec.validate_pos, "sideT", "10")

    def test_validate_positionv(self):
        self.assertRaises(ValueError, self.rec.validate_pos, "sideV", -100)

    def test_update(self):
        rec = self.rec
        self.rec.update(10, 10, 10, 10, 10)
        self.assertEqual([rec.id, rec.width, rec.height, rec.x, rec.y],
                         [10, 10, 10, 10, 10])

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
