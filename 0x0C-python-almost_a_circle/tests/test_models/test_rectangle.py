#!/usr/bin/python3
'''Test module for ``rectangle.py``.
'''
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Class for testing successful instantiation of Rectangle.
    '''

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(12, -6)
        self.r5 = Rectangle(-10, -20)

    def test_attr(self):
        '''Tests for correct attribute assignment.'''
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r4.height, -6)
        self.assertEqual(self.r5.x, 0)

    def test_private(self):
        '''Test for inaccessibilty of private attribute.'''
        with self.assertRaises(AttributeError):
            self.r1.__x
