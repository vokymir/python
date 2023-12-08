import random
import unittest
import typing
import builtins
import re
from typing import Optional
from typing import Any

from primes import * 

class PrimeTest(unittest.TestCase):

    class InputShim:
        """
        TĹ™Ă­da pro nahrazenĂ­ standardnĂ­ funkce input pro vstup dat
        """
        __idx:int = 0
        __lines:list[str] = []

        @staticmethod
        def set_input_data(lines:list[str]):
            PrimeTest.InputShim.__idx = 0
            PrimeTest.InputShim.__lines = lines
            builtins.input = typing.cast(Any, PrimeTest.InputShim.__next)

        @staticmethod
        def get_latest_input() -> Optional[str]:
            if PrimeTest.InputShim.__idx==0:
                return None
            else:
                return PrimeTest.InputShim.__lines[PrimeTest.InputShim.__idx-1]        

        @staticmethod
        def __next(prompt:str=""):
            assert PrimeTest.InputShim.__idx<len(PrimeTest.InputShim.__lines), "| nejsou zadany dalsi hodnoty na vstupu"
            result = PrimeTest.InputShim.__lines[PrimeTest.InputShim.__idx]
            PrimeTest.InputShim.__idx += 1
            return result
        
    def is_prime_assert(self, n: int, expected: bool):
        """
        JednoduchĂˇ funkce, kterĂˇ otestuje, zda is_prime pro zadane cislo vraci odpovidajici odpoved
        """
        actual = is_prime(n)
        self.assertEqual(actual,expected, f"| For: {n}")

    def test_is_prime_predefined(self):
        """
        Test pro sadu preddefinovanych cisel
        """
        self.is_prime_assert(1, False)
        self.is_prime_assert(2, True)
        self.is_prime_assert(3, True)
        self.is_prime_assert(4, False)
        self.is_prime_assert(5, True)
        self.is_prime_assert(9, False)
    
    def test_is_prime_not_prime(self):
        """
        Test pro sada nahodnych neprvocisel
        """
        for i in range(0,3):
            a = random.randint(500,1000)
            b = random.randint(500,1000)
            self.is_prime_assert(a*b, False)

    def test_is_prime_prime(self):
        """
        Test pro sadu nahodnych prvocisel z intervalu [23..44]
        """
        for i in range(0,3):
            a = random.randint(23,44)
            self.is_prime_assert(36*a*a - 810*a + 2753, True)
            

    def test_is_sum_of_primes_exists(self):
        """
        Test funkce is_sum_of_primes.
        Predpoklada, ze is_prime funguje. 
        """
        numbers = [13, 21, 69]
        for i in range(4):
            numbers.append(random.randint(2,100000) * 2)

        for number in numbers:
            prime = is_sum_of_primes(number)
            self.assertTrue(prime>0, "|Nenasel soucet pro {number}")
            self.assertTrue(is_prime(prime), "|Clen souctu pro {number} neni prvocislo")
            self.assertTrue(is_prime(number-prime), "|Clen souctu pro {number} neni prvocislo")
            self.assertTrue(prime >= number-prime, "|Pro {number} je vraceny clen souctu mensi")

    def generate_non_sum_number(self):
        """
        Funkce predpoklada spravnost funkce is_prime.
        """
        number = 4
        while is_prime(number-2):
            number = random.randint(1,10000) * 2 + 1
        return number

    def test_is_sum_of_primes_not_exists(self):
        """
        Test funkce is_sum_of_primes pro cisla, ktera nelze secist
        """
        numbers = [2,3,11,27]

        for i in range(4):
            numbers.append(self.generate_non_sum_number())

        for number in numbers:
            prime = is_sum_of_primes(number)
            self.assertTrue(prime==0,f"|Pro cislo {number} neexistuje soucet")


    def input_natural_number_assert(self,inputs:list[str],expected:int):
        """
        Jednoducha funkce, ktera otestuje zadana cisla pro vstup prirozeneho cisla
        """ 
        PrimeTest.InputShim.set_input_data(inputs)
        actual = input_natural_number()
        self.assertEqual(expected,actual,f"| Chybne zpracovani vstupu: {PrimeTest.InputShim.get_latest_input()}")

    def test_input_natural_number(self):
        """
        Test preddefinovane sady cisel pro vstup 
        """
        self.input_natural_number_assert(["1"],1)
        self.input_natural_number_assert(["-1","2"],2)
        self.input_natural_number_assert(["-5","0","-3","8"],8)
    