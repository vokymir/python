from vector2 import Vector2
from gui import Gui

class World:
    """
    Stores the terrain, map except game objects. Can draw it to the gui map, also can check if position is empty.

    Jakub Vokoun
    26.11.2023
    """
    @property
    def width(self) -> int:
        return self.__width
    @property
    def height(self) -> int:
        return self.__height
    
    @property
    def background(self) -> str:
        return self.__symbols[0]
    

    def __init__(self, data:list[list[int]], symbols:list[str]) -> None:
        """
        Creates a terrain map.

        Args:
            data: List of rows, each row is list of ints. Each int is later represented by symbols.
            symbols: List of chars, symbol on position 0 will replace 0 in terrain map, etc. Also symbol on 0 is background, others are collidable and inflict death to hero.
        """
        self.__height = len(data)
        self.__width = len(data[0])
        self.__data = data
        self.__symbols = symbols

    def is_empty(self, position:Vector2) -> bool:
        if self.__data[position.y][position.x] == 0:
            return True
        return False
    
    def draw(self, gui:Gui):
        """
        Draws the terrain into Gui. Takes 2D int array and converts it into 2D str array by "__symbols" arr.
        """
        for row in range(self.height):
            for col in range(self.width):
                symb:str =""
                for sym in range(len(self.__symbols)):
                    if sym == self.__data[row][col]:
                        symb += self.__symbols[sym]
                        break
                gui.draw(col,row,symb)
