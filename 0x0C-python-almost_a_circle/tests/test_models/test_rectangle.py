#!/usr/bin/python3
'''Test module for ``rectangle.py``.
'''
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io
import sys
import json


class TestRectangle(unittest.TestCase):
    '''Class for testing successful instantiation of Rectangle.
    '''

    def setUp(self):
        Rectangle.reset_nb()
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 20)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(10, 2, 3)

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
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 2, 1, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

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
        self.assertRaises(TypeError, Rectangle, 1,
 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_area(self):
        '''Tests for value of area
        '''
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 40)
        self.assertNotEqual(self.r2.area(), 22)

    def test_str(self):
        '''Tests the string representation
        '''
        self.assertEqual(str(self.r3), "[Rectangle] (12) 0/0 - 10/2")

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

    def test_display(self):
        '''Tests  display
        '''
        captured_out = io.StringIO()  # create a StringIO object
        sys.stdout = captured_out  # redirect stdout to the StringIO object
        self.r1.display()  # produce the output to capture
        self.assertEqual(captured_out.getvalue(), "##########\n##########\n")
        sys.stdout = sys.__stdout__  # reset to default terminal file object
        self.assertEqual(self.r4.display(), None)
        self.assertEqual(self.r3.display(), None)

    def test_to_dictionary(self):
        '''Tests for proper conversion of Rectangle object to dictionary
        '''
        self.assertEqual(self.r1.to_dictionary(), dict(width=10, height=2, x=0, y=0, id=1))
        self.assertEqual(self.r4.to_dictionary(), dict(width=10, height=2, x=3, y=0, id=3))

    def test_create(self):
        '''Test for proper creation of Rectangle instances
        '''
        self.assertIs(type(Rectangle.create(**{"id": 89})), Rectangle)
        self.assertIs(type(Rectangle.create(**{"id": 89, "width": 1})), Rectangle)
        self.assertIs(type(Rectangle.create(**{"id": 89, "width": 1, "height": 2})), Rectangle)
        self.assertIs(type(Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})), Rectangle)
        self.assertIs(type(Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})), Rectangle)
        self.assertEqual(Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}).height, 2)

    def test_save_to_file(self):
        '''Tests for success of state save
        '''
        Rectangle.save_to_file([self.r1])
        try:
            with open("Rectangle.json", 'r', encoding='utf-8') as fin:
                s = fin.read()
                self.assertEqual(json.loads(s), [{"width": 10, "height": 2, "x": 0, "y": 0, "id": 1}])
        except FileNotFoundError:
            self.fail("state not saved to json file")
        Rectangle.save_to_file([])
        try:
            with open("Rectangle.json", 'r', encoding='utf-8') as fin:
                s = fin.read()
                self.assertEqual(json.loads(s), [])
        except FileNotFoundError:
            self.fail("state not saved to json file")
        Rectangle.save_to_file(None)
        try:
            with open("Rectangle.json", 'r', encoding='utf-8') as fin:
                s = fin.read()
                self.assertEqual(json.loads(s), [])
        except FileNotFoundError:
            self.fail("state not saved to json file")

    def test_load_from_file(self):
        '''Tests for correct deserialization from json file
        '''
        inst = Rectangle.load_from_file()
        self.assertIs(type(inst), list)
