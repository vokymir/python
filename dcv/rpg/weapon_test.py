import random
import unittest
from weapon import Weapon

class WeaponTest(unittest.TestCase):
    def assertWeapon(self, weapon:Weapon, name:str, attack:int, defense: int, msg:str):
        text = f"{name} [{attack}/{defense}]"
        self.assertEqual(text, weapon.__str__(), msg)

    def test_weapon(self):
        attack = random.randrange(100)
        defense = random.randrange(100)
        weapon = Weapon("Zbran", attack, defense)
        self.assertEqual(defense, weapon.defense, "|Vytvorena zbran ma jinou obranu, nez s jakou byla vytvorena.")
        self.assertEqual(attack, weapon.attack, "|Vytvorena zbran ma jiny utok, nez s jakym byla vytvorena.")
        self.assertWeapon(weapon,"Zbran",attack,defense, "|Vytvorena zbran se lisi od zadani")

