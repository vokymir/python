
class Item:
    def __init__(self, name:str, pricePerUnit:float, units:int) -> None:
        self.__name = name
        self.__pricePerUnit = pricePerUnit
        self.__units = units

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def pricePerUnit(self) -> float:
        return self.__pricePerUnit
    
    @property
    def units(self) -> int:
        return self.__units
    
    @units.setter
    def units(self, units:int):
        if units > 0:
            self.__units = units

    @property
    def priceTotal(self):
        return self.__units * self.__pricePerUnit
    
    def __str__(self) -> str:
        """
        Returns as assigned: 
        rohlik    5 Kc    2 ks    10 Kc
        """
        return f"{self.__name}\t{self.pricePerUnit:.2f} Kc\t{self.__units} ks\t{self.priceTotal} Kc"