import unittest
from lab1 import get_roots

class SquareEqSolverTestCase(unittest.TestCase):
   def test_no_root(self):
       res = get_roots(1, 11, 10)
       self.assertEqual(len(res), 0)

   def test_single_root(self):
       res = get_roots(10, 0, 0)
       self.assertEqual(len(res), 1)
       self.assertEqual(res, [0])

   def test_two_roots(self):
       res = get_roots(1, -2, -8)
       self.assertEqual(len(res), 2)
       self.assertEqual(res, [-2, 2])

   def test_three_roots(self):
       res = get_roots(-4, 16, 0)
       self.assertEqual(len(res), 3)
       self.assertEqual(res, [-2, 0, 2])

   def test_four_roots(self):
       res = get_roots(1, -10, 9)
       self.assertEqual(len(res), 4)
       self.assertEqual(res, [-3, -1, 1, 3])