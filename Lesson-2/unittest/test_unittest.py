# by Daniel Rodriguez Amezaga
# 5 tests with unittest for the file funciones.py
# python -m pip install unittest2 

import unittest 
from functions import calculateAverage

'''
.assertEqual(a, b): Verifies the equality of both values.
.assertTrue(x): Verifies that the value is True.
.assertFlase(x): Verifies that the value is Flase.
.assertIs(a, b): Verifies that both variables are the same.
.assertIsNone(x): Verifies that the value is None.
.assertIn(a, b): Verifies that a belongs to iterable b.
.assertIsInstance(a, b): Verifies that a is an instance of b.
.assertRaises(x): Verifies that an exception is thrown.
'''

class TestMedia(unittest.TestCase):
    def setUp(self):
        print("Entering setUp")
    
    def tearDown(self):
        print("Entering tearDown.")
        
    # The name of the method must be test_<loquesea>.
    def test_calculateAverage(self):
            result = calculateAverage([20,20,20,20])
            self.assertEqual(result,20)
            
    def test_calculateGreater(self):
            self.assertGreater(20,10)
            
    def test_calculateLess(self):
            self.assertLess(5,10)
            
    def test_calculateEqual(self):
            self.assertEqual(20,20)
           
    def test_calculateDifferent(self):
            self.assertNotEqual(20,0)
    
    def test_greater_or_equal(self):
        self.assertNotAlmostEqual(20,0)