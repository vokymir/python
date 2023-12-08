import unittest
import random

from vector2 import Vector2
from gameobject import GameObject
from gui import Gui

class GameObjectTest(unittest.TestCase):
    def test_draw(self):
        def mock_draw(tx:int, ty:int, tc:str):
            self.assertEqual(x,tx)
            self.assertEqual(y,ty)
            self.assertEqual(c,tc)

        x = random.randrange(1,100)
        y = random.randrange(1,100)
        c = chr(random.randint(65,90))
        obj = GameObject(Vector2(x,y), c)

        gui = Gui(100,100)
        gui.draw = mock_draw
        obj.draw(gui)

    def test_move(self):
        def mock_draw(tx:int, ty:int, tc:str):
            self.assertEqual(x,tx)
            self.assertEqual(y,ty)
            self.assertEqual(c,tc)

        x = random.randrange(1,100)
        y = random.randrange(1,100)
        mx = random.randrange(1,10)
        my = random.randrange(1,10)
        c = chr(random.randint(65,90))
        obj = GameObject(Vector2(x,y), c)
        
        gui = Gui(100,100)
        gui.draw = mock_draw
        obj.draw(gui)

        obj.move(Vector2(mx,my))
        x += mx
        y += my
        obj.draw(gui)
