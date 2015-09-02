import unittest
from stringcalculator import Stringcalculator as sc

class TestStringcalculator(unittest.TestCase):

    def test_add_withEmptyString_returnsZero(self):
        self.assertEqual(sc.add(""), 0)

    def test_add_with1_returns1(self):
        self.assertEqual(sc.add("1"), 1)

    def test_add_with4_returns4(self):
        self.assertEqual(sc.add("4"), 4)

    def test_add_with1and3_returns4(self):
        self.assertEqual(sc.add("1,3"), 4)

    def test_add_with1and5_returns6(self):
        self.assertEqual(sc.add("1,5"), 6)
