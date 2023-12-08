from weapon import *

class Character:
    """
    Character with name, strength, agility and vitality. Vitality = HP, agility = defense modifier, strength = attack modifier.


    Author: Jakub Vokoun
    Date: 23.11.2023
    """
    def __init__(self, name:str, strength:int, agility:int, vitality:int) -> None:
        """
        Inits a new character:

        args:
            name: Name of a hero.
            strength: stregth (attack modifier)
            agility: agility (defense modifier)
            vitality: HP
        """
        self.__name = name
        self.__strength = strength
        self.__agility = agility
        self.__vitality = vitality
        self.Hand_left_weapon = Weapon("None",0,0)
        self.Hand_right_weapon = Weapon("None",0,0)
        self.HAND_LEFT_equipped = False
        self.HAND_RIGHT_equipped = False
    
    HAND_LEFT:int = 0
    HAND_RIGHT:int = 1
    HAND_LEFT_equipped:bool = False
    HAND_RIGHT_equipped:bool = False


    def attack(self) -> int:
        """
        Calculates combined attack value of a hero -> strength + attack of weapon in right and left hands.

        Returns:
            Combined attack value.
        """
        if self.HAND_LEFT_equipped:
            left = self.Hand_left_weapon.attack
        else:
            left = 0
        if self.HAND_RIGHT_equipped:
            right = self.Hand_right_weapon.attack
        else:
            right = 0
        return self.__strength + left + right
    
    def armor(self) -> int:
        """
        Calculates combined defense value of hero and his/her weapons.

        Returns:
            Combined defense of a hero.
        """
        if self.HAND_LEFT_equipped:
            left = self.Hand_left_weapon.defense
        else:
            left = 0
        if self.HAND_RIGHT_equipped:
            right = self.Hand_right_weapon.defense
        else:
            right = 0
        return left + right + self.__agility

    def defend(self, attack:int) -> int:
        """
        Returns damage you get, but if negative, than 0. Also changes vitality.
        """
        damage:int = attack - self.armor()
        if damage > 0:
            self.__vitality -= damage
            return damage
        else:
            return 0
    
    def is_alive(self) -> bool:
        return self.__vitality > 0
    
    def take_weapon(self, weapon:Weapon|None, hand:int) -> bool:
        """
        Checks if *hand* with index hand is empty, if so it equips hero the suggested weapon and returns true.
        Otherwise it just returns False
        """
        if hand == self.HAND_LEFT and not(self.HAND_LEFT_equipped) and type(weapon) == Weapon:
            self.Hand_left_weapon = weapon
            self.HAND_LEFT_equipped = True
            return True
        elif hand == self.HAND_RIGHT and not(self.HAND_RIGHT_equipped) and type(weapon) == Weapon:
            self.Hand_right_weapon = weapon
            self.HAND_RIGHT_equipped = True
            return True
        return False
    
    def __str__(self) -> str:
        return f"{self.__name} [{self.__vitality}] ({self.attack()}/{self.armor()})"
    