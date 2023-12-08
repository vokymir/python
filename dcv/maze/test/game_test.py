import unittest
import builtins
import typing
from typing import Any
from typing import Optional

from game import Game
from world import World
from gameobject import GameObject
from vector2 import Vector2

class GameTest(unittest.TestCase):
    class InputShim:
        """
        Třída pro nahrazení standardní funkce input pro vstup dat
        """
        __idx:int = 0
        __lines:list[str] = []

        @staticmethod
        def set_input_data(lines:list[str]):
            GameTest.InputShim.__idx = 0
            GameTest.InputShim.__lines = lines
            builtins.input = typing.cast(Any, GameTest.InputShim.__next)

        @staticmethod
        def get_latest_input() -> Optional[str]:
            if GameTest.InputShim.__idx==0:
                return None
            else:
                return GameTest.InputShim.__lines[GameTest.InputShim.__idx-1]        

        @staticmethod
        def __next(prompt:str=""):
            assert GameTest.InputShim.__idx<len(GameTest.InputShim.__lines), "| nejsou zadany dalsi hodnoty na vstupu"
            result = GameTest.InputShim.__lines[GameTest.InputShim.__idx]
            GameTest.InputShim.__idx += 1
            return result

    def test_run_lost(self):
        world = World(
            [[1,1,1,1],
             [1,0,0,1],
             [1,1,1,1]],
             [' ','#'])
        hero = GameObject(Vector2(1,1),"@")
        home = GameObject(Vector2(2,1),"^")
        GameTest.InputShim.set_input_data("4")
        self.assertFalse(Game(world,hero,home).run())

    def test_run_home(self):
        world = World(
            [[1,1,1,1],
             [1,0,0,1],
             [1,1,1,1]],
             [' ','#'])
        hero = GameObject(Vector2(1,1),"@")
        home = GameObject(Vector2(2,1),"^")
        GameTest.InputShim.set_input_data("6")
        self.assertTrue(Game(world,hero,home).run())

