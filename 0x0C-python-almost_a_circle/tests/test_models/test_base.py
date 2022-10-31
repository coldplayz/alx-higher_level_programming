#!/usr/bin/python3
'''Test module for ``base.py``.
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Class for testing proper id allocation of Base instances.
    '''

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
        self.b6 = Base(-5)

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5
        del self.b6

    def test_id(self):
        '''Tests for correct id assignment.'''
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
        self.assertEqual(self.b6.id, -5)

    def test_private(self):
        '''Test for inaccessibilty of private attribute.'''
        with self.assertRaises(AttributeError):
            Base.__nb_objects
