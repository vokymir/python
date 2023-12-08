from factorial import *
import unittest

class FactorialTest(unittest.TestCase):

    def fact_assert(self, n: int, expected: int):
        """
        Obalovaci funkce, ktera porovna, zda testovana funkce odpovi ocekavanou hodnotou
        Zjednodusi nam testovani vice ruznych hodnot
        """
        actual = fact(n)
        self.assertEqual(actual,expected, f"| For: {n}")
        

    def test_fact(self):
        """
        Samotny test, ktery se spousti testovacim nastrojem
        """
        self.fact_assert(1,1)
        self.fact_assert(3,6)
        self.fact_assert(5,120)
