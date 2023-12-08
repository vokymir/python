import random
import unittest
import builtins
import typing
from typing import Any
from character import Character
from weapon import Weapon
from rpg import RPG

class RPGTest(unittest.TestCase):

    class InputShim:
        """
        Třída pro nahrazení standardní funkce input pro vstup dat
        """
        __idx:int = 0
        __lines:list[str] = []

        @staticmethod
        def set_input_data(lines:list[str]):
            RPGTest.InputShim.__idx = 0
            RPGTest.InputShim.__lines = lines
            builtins.input = typing.cast(Any, RPGTest.InputShim.__next)

        @staticmethod
        def get_latest_input() -> str|None:
            if RPGTest.InputShim.__idx==0:
                return None
            else:
                return RPGTest.InputShim.__lines[RPGTest.InputShim.__idx-1]        

        @staticmethod
        def __next(prompt:str=""):
            assert RPGTest.InputShim.__idx<len(RPGTest.InputShim.__lines), "| nejsou zadany dalsi hodnoty na vstupu"
            result = RPGTest.InputShim.__lines[RPGTest.InputShim.__idx] # + "\n"
            RPGTest.InputShim.__idx += 1
            return result
    """
    class PrintShim:

        @staticmethod
        def set_output_data():
            builtins.print = 

            """

    def assertCharacter(self, char:Character, name:str, vitality:int, attack:int, defense:int, msg:str):
        text = f"{name} [{vitality}] ({attack}/{defense})"
        self.assertEqual(text, char.__str__(), msg)

    def assertWeapon(self, weapon:Weapon|None, name:str, attack:int, defense: int, msg:str):
        text = f"{name} [{attack}/{defense}]"
        self.assertEqual(text, weapon.__str__(), msg)


    def test_input_character(self):
        strength = random.randrange(1,50)
        agility = random.randrange(1,50)
        vitality = random.randrange(1,50)
        name = "nactiPostavu"
        RPGTest.InputShim.set_input_data([name,str(strength),str(agility),str(vitality)])
        rpg = RPG()
        char = rpg.input_character()
        self.assertCharacter(char, name, vitality, strength, agility, "|Nactena postava tvrdi, ze ma jine vlastnosti, nez by mela mit.")

    def test_input_weapon(self):
        defense = random.randrange(1,50)
        attack = random.randrange(1,50)
        name = "nactiZbran"
        RPGTest.InputShim.set_input_data([name,str(attack),str(defense)])
        rpg = RPG()
        weapon = rpg.input_weapon()
        self.assertWeapon(weapon,name,attack,defense,"|Nactena zbran tvrdi, ze ma jine vlastnosti, nez by mela mit.")

        RPGTest.InputShim.set_input_data([""])
        rpg = RPG()
        weapon = rpg.input_weapon()
        self.assertIsNone(weapon, "|Nemela se nacist zadna zbran")

    def test_equip_character(self):
        strength = random.randrange(1,50)
        attackL = random.randrange(1,50)
        attackR = random.randrange(1,50)
        agility = random.randrange(1,50)
        defenseL = random.randrange(1,50)
        defenseR = random.randrange(1,50)
        vitality = random.randrange(1,50)
        name = "vyzbrojPostavu"
        char = Character(name,strength,agility,vitality)
        left = Weapon("leva",attackL,defenseL)
        right = Weapon("prava",attackR,defenseR)

        rpg = RPG()
        rpg.equip_character(char,None,right)
        self.assertCharacter(char,name,vitality,strength+attackR, agility + defenseR,"|Vyzbrojeni postavy se nepovedlo, cekal jsem jiny utok.")

        rpg.equip_character(char,left,None)
        self.assertCharacter(char,name,vitality,strength+attackR+attackL, agility + defenseR+defenseL,"|Vyzbrojeni postavy se nepovedlo, cekal jsem jiny utok.")

    def test_fight(self):
        char1=Character("Golias",3,0,10)
        char2=Character("David",1,1,20)
        c1s = char1.__str__()
        c2s = char2.__str__()

        rpg = RPG()
        winner = rpg.fight(char1, char2)
        self.assertEqual(winner, char1, f"|{c1s} zautocil na {c2s} a mel vyhrat")

        char1=Character("Golias",3,0,10)
        char2=Character("David",1,1,20)
        c1s = char1.__str__()
        c2s = char2.__str__()

        rpg = RPG()
        winner = rpg.fight(char2, char1)
        self.assertEqual(winner, char2, f"|{c2s} zautocil na {c1s} a mel vyhrat")

