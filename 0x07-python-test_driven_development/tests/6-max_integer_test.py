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

    def test_max_start(self):
        self.assertEqual(max_integer([9, 1, 4, 0]), [9, 1, 4, 0][0])

    def test_max_end(self):
        self.assertEqual(max_integer([1, 4, 0, 9]), [1, 4, 0, 9][3])

    def test_neg_single(self):
        self.assertEqual(max_integer([9, 1, -4, 0]), 9)

    def test_neg_all(self):
        self.assertEqual(max_integer([-9, -1, -4, -57]), -1)

    def test_singleton(self):
        self.assertEqual(max_integer([5]), 5)
