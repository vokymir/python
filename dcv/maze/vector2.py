from __future__ import annotations

class Vector2:
    """
    2D vector (x,y)

    Jakub Vokoun
    26.11.2023
    """

    @property
    def x(self) -> int:
        return self.__x
    
    @property
    def y(self) -> int:
        return self.__y
    

    def __init__(self, x:int, y:int) -> None:
        self.__x = x
        self.__y = y

    
    def __add__(self, other:Vector2) -> Vector2:
        x:int = self.x + other.x
        y:int = self.y + other.y
        return Vector2(x, y)
    
    def __eq__(self, other) -> bool:
        if type(other) == Vector2:
            if self.x == other.x and self.y == other.y:
                return True
        return False
    
    def __str__(self) -> str:
        return f"{self.x}; {self.y}"