#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Class for ``max_integer`` TestCase instances
    '''

    data = [1, 9, 4, 0]

    def test_result_correct(self):
        self.assertEqual(max_integer(TestMaxInteger.data), 9)
        self.assertEqual(max_integer([]), None)

    def test_result_wrong(self):
        self.assertNotEqual(max_integer(TestMaxInteger.data), 0)

    def test_result_type(self):
        self.assertIsInstance(max_integer(TestMaxInteger.data), int)
