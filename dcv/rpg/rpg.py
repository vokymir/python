from character import *

class RPG:
    """
    Hlavní třída, která načte z klávesnice informace o první postavě, zbrani do levé a zbrani do pravé ruky. Následně načte stejné informace o druhé postavě.
    Poté spustí souboj mezi postavami (1. postava útočí, 2. postava se brání a opačně), dokud některé z postav neklesne zdraví pod 1.
    Na konci musí aplikace vypsat informace o vítězi: (viz Character.__str__()).
    
    Author: Jakub Vokoun
    Date: 24.11.2023
    """
    def input_character(self) -> Character:
        """
        Ze standardního vstupu načte postupně jméno, sílu, hbitost a zdraví a vytvoří novou postavu. Každý údaj je na samostatné řádce.
        """
        name:str = input("Enter name: ")
        strength:int = int(input("Enter strength: "))
        agility:int = int(input("Enter agility: "))
        vitality:int = int(input("Enter vitality: "))
        return Character(name,strength, agility, vitality)

    def input_weapon(self) -> Weapon|None:
        """
        Ze standardního vstupu načte postupně název, útočnou a obrannou sílu a vytvoří novou zbraň. Pokud se zadá prázdný název, metoda okamžitě vrátí hodnotu None (zbytek informací nenačítá). Každý údaj je na samostatné řádce.
        """
        name:str = input("Enter weapon name: ")
        if name == "":
            return None
        attack:int = int(input("Enter weapon attack: "))
        defense:int = int(input("Enter weapon defense: "))
        return Weapon(name, attack, defense)

    def equip_character(self, character:Character, left:Weapon|None, right:Weapon|None):
        """
        Vyzbrojí postavu dodanými zbraněmi. Pokud již postava nějakou zbraň měla, zůstane jí (viz Character.take_weapon). Obecně může být zbraň None.
        """
        character.take_weapon(left,character.HAND_LEFT)
        character.take_weapon(right,character.HAND_RIGHT)
        return character

    def fight(self, character1:Character, character2:Character) -> Character:
        """
        Spustí souboj mezi postavami. Souboj končí v okamžiku, kdy zdraví některé z postav klesne pod 1. Útočit začíná character1. Útok probíhá tak, že se zjistí síla útoku útočící postavy (viz Character.attack) a bránící se postava se pokusí tomuto útoku ubránit (viz Character.defend()). Metoda vrátí přeživší postavu.
        """
        while True:
            print(f"{character1} utoci a zpusobuje {character2.defend(character1.attack())} zraneni")
            if not(character2.is_alive()):
                return character1
            print(f"{character2} utoci a zpusobuje {character1.defend(character2.attack())} zraneni")
            if not(character1.is_alive()):
                return character2


    def run(self):
        """
        Spustí celou hru. Načte první postavu a zbraň pro levou a pravou ruku. Načte druhou postavu a zbraň pro levou a pravou ruku. Obě postavy vyzbrojí a spustí souboj, ve kterém začíná útočit první postava. Po ukončení souboje vypíše informace o vítězi ve formátu Vitez: {postava}.
        """
        hero1 = rpg.input_character()
        rpg.equip_character(hero1, rpg.input_weapon(), rpg.input_weapon())
        
        hero2 = rpg.input_character()
        rpg.equip_character(hero2, rpg.input_weapon(), rpg.input_weapon())

        print(f"Vitez: {rpg.fight(hero1,hero2)}")


if __name__ == "__main__":
    rpg = RPG()
    rpg.run()