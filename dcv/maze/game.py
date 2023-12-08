from world import World
from gui import Gui
from gameobject import GameObject
from vector2 import Vector2

class Game:
    """
    The Maze game itself, callable by run().
    
    Jakub Vokoun
    26.11.2023
    """
    def __init__(self, world: World, hero: GameObject, home: GameObject):
        """
        Creates a game.

        Args:
            world: Terrain map, created by World().
            hero: Movable unit, created by GameObject().
            home: Immovable, created by GameObject().
        """
        self.__world = world
        self.__hero = hero
        self.__home = home

    def run(self) -> bool:
        """
        Inits a game, places home and hero on the map.
        Loops until hero either comes home (True) or collides with walls (False).
        Every iteration moves hero, checks if the game comes to its end and if not, asks for directions.
        """
        gui = Gui(self.__world.width, self.__world.height)
        homeX = self.__home.position.x
        homeY = self.__home.position.y
        heroSym:str = self.__hero.symbol
        # ajajaj is for colliding with objects
        ajajaj:bool = False
        self.__world.draw(gui)
        gui.draw(homeX, homeY, self.__home.symbol)

        while True:
            currX:int = self.__hero.position.x
            currY:int = self.__hero.position.y

            if not self.__world.is_empty(Vector2(currX,currY)):
                ajajaj = True
            
            gui.draw(currX, currY, heroSym)
            gui.show()

            if currX == homeX and currY == homeY:
                return True
            elif currX == 0 or currX == gui.width or currY == 0 or currY == gui.height or ajajaj:
                return False
            
            #moves hero and cleares the place he was before
            self.__hero.move(gui.input_direction())
            gui.draw(currX, currY, self.__world.background)




if __name__ == "__main__":
    world = World(
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

        ['⬛','💀'])
    hero = GameObject(Vector2(1,1),"🧓")
    home = GameObject(Vector2(4,1),"🪦 ")

    destination = Game(world,hero,home).run()
    if destination: 
        print("Vitej doma!")
    else:
        print("... a uz ho nikdy nikdo nevidel... ")
