#!/usr/bin/python3
'''Test module for ``base.py``.
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Class for testing proper id allocation of Base instances.
    '''

    @classmethod
    def setUpClass(cls):
        cls.Base2 = type("Base2", (Base,), dict(Base.__dict__))

    def setUp(self):
        self.b1 = self.__class__.Base2()
        self.b2 = self.__class__.Base2()
        self.b3 = self.__class__.Base2()
        self.b4 = self.__class__.Base2(12)
        self.b5 = self.__class__.Base2()

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5

    def test_id(self):
        '''Tests for correct id assignment.'''
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
        self.assertRaises(TypeError, self.__class__.Base2, "5")

    def test_private(self):
        '''Test for inaccessibilty of private attribute.'''
        with self.assertRaises(AttributeError):
            self.__class__.Base2.__nb_objects
