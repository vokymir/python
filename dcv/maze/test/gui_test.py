import unittest
import random
import builtins
import typing
from typing import Any
from typing import Optional

from gui import Gui
from vector2 import Vector2

class GuiTest(unittest.TestCase):
    class InputShim:
        """
        Třída pro nahrazení standardní funkce input pro vstup dat
        """
        __idx:int = 0
        __lines:list[str] = []

        @staticmethod
        def set_input_data(lines:list[str]):
            GuiTest.InputShim.__idx = 0
            GuiTest.InputShim.__lines = lines
            builtins.input = typing.cast(Any, GuiTest.InputShim.__next)

        @staticmethod
        def get_latest_input() -> Optional[str]:
            if GuiTest.InputShim.__idx==0:
                return None
            else:
                return GuiTest.InputShim.__lines[GuiTest.InputShim.__idx-1]        

        @staticmethod
        def __next(prompt:str=""):
            assert GuiTest.InputShim.__idx<len(GuiTest.InputShim.__lines), "| nejsou zadany dalsi hodnoty na vstupu"
            result = GuiTest.InputShim.__lines[GuiTest.InputShim.__idx]
            GuiTest.InputShim.__idx += 1
            return result

    def test_input_direction(self):
        gui = Gui(1,1)

        GuiTest.InputShim.set_input_data("2")
        v = gui.input_direction()
        self.assertEqual(Vector2(0,1),v)

        GuiTest.InputShim.set_input_data("4")
        v = gui.input_direction()
        self.assertEqual(Vector2(-1,0),v)

        GuiTest.InputShim.set_input_data("8")
        v = gui.input_direction()
        self.assertEqual(Vector2(0,-1),v)

        GuiTest.InputShim.set_input_data("6")
        v = gui.input_direction()
        self.assertEqual(Vector2(1,0),v)

        GuiTest.InputShim.set_input_data("9")
        v = gui.input_direction()
        self.assertEqual(Vector2(0,0),v)

    

