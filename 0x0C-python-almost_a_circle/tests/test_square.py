#!/usr/bin/python3
"""Square class tests"""

import unittest
from models import Square

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
