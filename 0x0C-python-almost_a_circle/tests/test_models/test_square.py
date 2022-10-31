#!/usr/bin/python3
'''Test module for ``rectangle.py``.
'''
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Class for testing successful instantiation of Sqaure.
    '''

    def setUp(self):
        Square.reset_nb()
        self.s1 = Square(1, 2)
        self.s2 = Square(3, 4)
        self.s3 = Square(5, 6)

    def test_attr(self):
        '''Tests for correct attribute assignment.'''
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
