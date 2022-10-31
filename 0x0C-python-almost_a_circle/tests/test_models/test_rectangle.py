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

    def test_attr(self):
        '''Tests for correct attribute assignment.'''
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r1.height, 2)

    def test_private(self):
        '''Test for inaccessibilty of private attribute.'''
        with self.assertRaises(AttributeError):
            self.r1.__x

    def test_value_validation(self):
        '''Tests for proper input value validation
        '''
        with self.assertRaises(ValueError):
            Rectangle(12, -6)
        with self.assertRaises(ValueError):
            Rectangle(-10, 6)
        with self.assertRaises(ValueError):
            Rectangle(-12, -6)

    def test_type_validation(self):
        '''Tests for proper type validation
        '''
        with self.assertRaises(TypeError):
            Rectangle(12, "6")
        with self.assertRaises(TypeError):
            Rectangle([2, 4], 6)
        with self.assertRaises(TypeError):
            Rectangle(12, (1, 2))
        with self.assertRaises(TypeError):
            Rectangle({'a': 5}, 6)
        with self.assertRaises(TypeError):
            Rectangle(12, {13, 14})
        with self.assertRaises(TypeError):
            Rectangle(None, 6)
        with self.assertRaises(TypeError):
            Rectangle(12, 6.5)
        with self.assertRaises(TypeError):
            Rectangle(float("nan"), 6)
