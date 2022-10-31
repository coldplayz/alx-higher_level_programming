#!/usr/bin/python3
'''Test module for ``rectangle.py``.
'''
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    '''Class for testing successful instantiation of Rectangle.
    '''

    def setUp(self):
        Rectangle.reset_nb()
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 20)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def test_attr(self):
        '''Tests for correct attribute assignment.'''
        self.assertEqual(self.r1.id, 1)
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
        '''Tests for proper input type validation
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
        self.assertRaises(TypeError, Rectangle, float("nan"), 6)

    def test_area(self):
        '''Tests for value of area
        '''
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 40)
        self.assertNotEqual(self.r2.area(), 22)

    def test_str(self):
        '''Tests the string representation
        '''
        self.assertEqual(str(self.r3), "[Rectangle] (12) 0/0 10/2")

    def test_update(self):
        '''Tests for proper update
        '''
        self.r1.update(50)
        self.assertEqual(self.r1.id, 50)
        self.r2.update(3, 30)
        self.assertEqual(self.r2.width, 30)
        self.r3.update(100, 200, 10, 5, 37)
        self.assertEqual(self.r3.height, 10)
        self.assertEqual(self.r3.x, 5)
        self.assertEqual(self.r3.y, 37)
        self.assertEqual(self.r3.id, 100)
        self.assertRaises(TypeError, Rectangle, "50")
