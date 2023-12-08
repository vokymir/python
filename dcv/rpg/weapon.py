class Weapon:
    """
    Weapon object, has name, __attack and __defense, both privates are also properties.
    Also has __str__ >> name [attack/defense] => Voky [5/9]

    Author: Jakub Vokoun
    Date: 23.11.2023
    """
    def __init__(self, name:str, attack:int, defense:int) -> None:
        """
        Creates a weapon, with name, attack and defense.
        """
        self.__name = name
        self.__attack = attack
        self.__defense = defense
    
    @property
    def attack(self) -> int:
        return self.__attack
    
    @property
    def defense(self) -> int:
        return self.__defense
    
    def __str__(self) -> str:
        return f"{self.__name} [{self.__attack}/{self.__defense}]"