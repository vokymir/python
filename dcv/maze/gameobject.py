from vector2 import Vector2
from gui import Gui

class GameObject:
    """
    Object with its symbol, position and ability to move and draw itself to gui map.
    
    Jakub Vokoun
    26.11.2023
    """
    def __init__(self, position:Vector2, symbol:str) -> None:
        self.__position = position
        self.__symbol = symbol

    @property
    def position(self) -> Vector2:
        return self.__position
    
    @property
    def symbol(self) -> str:
        return self.__symbol
    
    def move(self, direction:Vector2):
        self.__position += direction
    
    def draw(self, gui:Gui):
        gui.draw(self.position.x, self.position.y, self.__symbol)