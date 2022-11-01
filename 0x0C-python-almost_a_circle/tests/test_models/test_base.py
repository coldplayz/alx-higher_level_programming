#!/usr/bin/python3
'''Test module for ``base.py``.
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Class for testing proper id allocation of Base instances.
    '''

    def setUp(self):
        Base2 = type("Base2", (Base,), dict(Base.__dict__))
        Base2.reset_nb()
        self.b1 = Base2()
        self.b2 = Base2()
        self.b3 = Base2()
        self.b4 = Base2(12)
        self.b5 = Base2()

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
        self.assertRaises(TypeError, Base, "5")

    def test_private(self):
        '''Test for inaccessibilty of private attribute.'''
        with self.assertRaises(AttributeError):
            self.__class__.Base.__nb_objects

    def test_to_json_string(self):
        '''Test for correct conversion to JSON
        '''
        self.assertEqual(self.b1.to_json_string(None), '[]')
        self.assertEqual(self.b2.to_json_string([]), '[]')
        self.assertEqual(self.b1.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        '''Test for correct conversion from JSON
        '''
        self.assertEqual(self.b1.from_json_string(None), [])
        self.assertEqual(self.b2.from_json_string('[]'), [])
        self.assertEqual(self.b3.from_json_string('[{"id": 89}]'), [{"id": 89}])
