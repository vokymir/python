from vector2 import Vector2

class Gui:
    """
    Stores a graphical representation of maze, can draw things on it, show it and clear it. 
    Also provides "graphical" communication with user by input_direction().

    Jakub Vokoun
    26.11.2023
    """

    def __init__(self, width:int, height:int) -> None:
        """
        The map is stored in 2D array. It's array of rows, and each row is array of individual chars.
        """
        self.__width = width
        self.__height = height
        self.__map:list = [[" " for i in range(width)] for j in range(height)]

    @property
    def width(self) -> int:
        return self.__width
    
    @property
    def height(self) -> int:
        return self.__height
    
    def draw(self, x:int, y:int, symbol:str):
        self.__map[y][x] = symbol

    def show(self):
        """
        Prints the whole maze to the console.
        """
        res:str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                res += str(self.__map[row][col])
            if row != (self.height-1):
                res += "\n"
        print(res)
    
    def clear(self):
        self.__map = [[" " for i in range(self.__width)] for j in range(self.__height)]

    def input_direction(self) -> Vector2:
        """
        4 = left; 6 = right, 2 = down, 8 = up, anything other = no movement
        """
        dir = Vector2(0,0)
        try:
            x = int(input())
        except:
            x = -1
        
        if x == 2:
            dir = Vector2(0,1)
        elif x == 4:
            dir = Vector2(-1,0)
        elif x == 6:
            dir = Vector2(1,0)
        elif x == 8:
            dir = Vector2(0,-1)
        
        return dir

