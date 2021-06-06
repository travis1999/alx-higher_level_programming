#!/usr/bin/python3
"""Tests for the rectangle class"""


import unittest
from models.rectangle import Rectangle


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
