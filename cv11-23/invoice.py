from item import *

class Invoice:
    def __init__(self) -> None:
        self.__items:list[Item] = []

    @property
    def priceTotal(self) -> float:
        total:float = 0.0
        for item in self.__items:
            total += item.priceTotal
        return total
    
    def addItem(self, item:Item):
        self.__items.append(item)

    def __str__(self) -> str:
        res:str = ""
        for item in self.__items:
            res += f"{item}\n"
        res += "-"*5 + "\n"
        res += f"soucet\t\t\t{self.priceTotal} Kc"
        return res