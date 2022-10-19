import doctest
import unittest


suite = unittest.TestSuite()
suite.addTest(doctest.DocFileSuite('101-lazy_matrix_mul.txt'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
