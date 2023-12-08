import random
import unittest
from character import Character
from weapon import Weapon

class CharacterTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.strength = random.randrange(1,50)
        self.attackL = random.randrange(1,50)
        self.attackR = random.randrange(1,50)
        self.agility = random.randrange(1,50)
        self.defenseL = random.randrange(1,50)
        self.defenseR = random.randrange(1,50)
        self.vitality = random.randrange(1,50)

    def assertCharacter(self, char:Character, name:str, vitality:int, attack:int, defense:int, msg:str):
        text = f"{name} [{vitality}] ({attack}/{defense})"
        self.assertEqual(text, char.__str__(), msg)

    def test_init(self):
        name = "Postava"
        text = f"{name} [{self.vitality}] ({self.strength}/{self.agility})"
        char = Character(name,self.strength,self.agility,self.vitality)
        self.assertCharacter(char, name, self.vitality, self.strength, self.agility,"|Postava o sobe nepodava spravne informace.")


    def test_take_weapon(self):
        name = "vezmiZbran"
        left = Weapon("LEVA", self.attackL, self.defenseL)
        right = Weapon("PRAVA", self.attackR, self.defenseR)
        char = Character(name, self.strength, self.agility, self.vitality)

        self.assertTrue(char.take_weapon(left,Character.HAND_LEFT),"|Postava tvrdi, ze si nemuze vzit zbran do prazdne leve ruky")
        self.assertCharacter(char,name,self.vitality,self.strength + self.attackL, self.agility + self.defenseL, "|Postava o sobe nepodava spravne informace")

        self.assertFalse(char.take_weapon(left,Character.HAND_LEFT),"|Postava tvrdi, ze si muze vzit zbran do plne leve ruky")
        self.assertCharacter(char,name,self.vitality,self.strength + self.attackL, self.agility + self.defenseL, "|Postava o sobe nepodava spravne informace")

        self.assertTrue(char.take_weapon(right,Character.HAND_RIGHT),"|Postava tvrdi, ze si nemuze vzit zbran do prazdne prave ruky")
        self.assertCharacter(char,name,self.vitality,self.strength + self.attackR + self.attackL, self.agility + self.defenseR + self.defenseL, "|Postava o sobe nepodava spravne informace")

        char = Character(name, self.strength, self.agility, self.vitality)

        self.assertTrue(char.take_weapon(right,Character.HAND_RIGHT),"|Postava tvrdi, ze si nemuze vzit zbran do prazdne prave ruky")
        self.assertCharacter(char,name,self.vitality,self.strength + self.attackR, self.agility + self.defenseR, "|Postava o sobe nepodava spravne informace")

        self.assertFalse(char.take_weapon(right,Character.HAND_RIGHT),"|Postava tvrdi, ze si muze vzit zbran do plne prave ruky")
        self.assertTrue(char.take_weapon(left,Character.HAND_LEFT), "|Postava tvrdi, ze si nemuze vzit zbran do prazdne leve ruky")

    def test_defend(self):
        name = "branSe"
        attack = random.randint(1,10)

        left = Weapon("LEVA", 0, self.defenseL)
        right = Weapon("PRAVA", 0, self.defenseR)

        char = Character(name, 0, self.agility, self.vitality)
        char.take_weapon(left,Character.HAND_LEFT)
        char.take_weapon(right, Character.HAND_RIGHT)

        self.assertTrue(0==char.defend(self.agility+self.defenseL+self.defenseR-1), "|Postava tvrdi, ze utrpela zraneni, i kdyz je utok mensi nez obrana")
        self.assertCharacter(char, name, self.vitality,0,self.agility+self.defenseL+self.defenseR,"|Postava o sobe nepodava spravne informace")

        self.assertTrue(0==char.defend(self.agility+self.defenseL+self.defenseR), "|Postava tvrdi, ze utrpela zraneni, i kdyz je utok mensi nez obrana")
        self.assertCharacter(char, name, self.vitality,0,self.agility+self.defenseL+self.defenseR,"|Postava o sobe nepodava spravne informace")

        self.assertTrue(attack==char.defend(self.agility+self.defenseL+self.defenseR+attack), "|Postava tvrdi, ze utrpela jine zraneni, nez mela")
        self.assertCharacter(char, name, self.vitality-attack,0,self.agility+self.defenseL+self.defenseR,"|Postava o sobe nepodava spravne informace")

    def test_attack(self):
        name = "zautoc"
        left = Weapon("LEVA", self.attackL, 0)
        right = Weapon("PRAVA", self.attackR, 0)

        char = Character(name, self.strength, 0, self.vitality)
        char.take_weapon(left,Character.HAND_LEFT)
        char.take_weapon(right, Character.HAND_RIGHT)

        self.assertTrue(self.strength + self.attackL + self.attackR == char.attack(), "|Postava tvrdi, ze utoci jinou silou, nez jaky je jeji utok.")
        self.assertCharacter(char, name, self.vitality, self.strength + self.attackL + self.attackR, 0, "|Postava o sobe nepodava spravne informace")

    def test_is_alive(self):
        name = "jeZiva"

        char = Character(name, 0,0,self.vitality)
        self.assertTrue(char.is_alive(), "|Postava zemrela pri narozeni")

        char.defend(self.vitality)
        self.assertFalse(char.is_alive(), "|Postava nezemrela pri brutalnim utoku")
