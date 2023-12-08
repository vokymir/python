import unittest
import random
from world import World
from vector2 import Vector2
from gui import Gui

class WorldTest(unittest.TestCase):

    def test_is_empty(self):
        width = random.randrange(5,10)
        height = random.randrange(5,10)
        data:list[list[int]] = []
        empty = []
        nonempty = []
        for y in range(height):
            data.append([])
            for x in range(width):
                val = random.randrange(5)
                data[y].append(val)
                if val==0:
                    empty.append(Vector2(x,y))
                else:
                    nonempty.append(Vector2(x,y))
            
        world = World(data, [' ']*5)
        for vec in empty:
            self.assertTrue(world.is_empty(vec))
        for vec in nonempty:
            self.assertFalse(world.is_empty(vec))

    def test_draw_horizontal(self):
        def mock_draw(tx:int, ty:int, tc:str):
            self.assertEqual(ty,0)
            self.assertEqual(tc, chr(65 + tx % 3))
            distinctX.add(tx)

        gui = Gui(100,100)
        gui.draw = mock_draw
        distinctX = set()

        tests = random.randint(10,20)
        data = [[i%3 for i in range(tests)]]
        world = World(data, [chr(65), chr(66), chr(67)])
        world.draw(gui)
        self.assertGreaterEqual(len(distinctX), tests)

    def test_draw_vertical(self):
        def mock_draw(tx:int, ty:int, tc:str):
            self.assertEqual(tx,0)
            self.assertEqual(tc, chr(80 + ty % 3))
            distinctY.add(ty)

        gui = Gui(100,100)
        gui.draw = mock_draw
        distinctY = set()

        tests = random.randint(10,20)
        data = [[i%3] for i in range(tests)]
        world = World(data, [chr(80), chr(81), chr(82)])
        world.draw(gui)
        self.assertGreaterEqual(len(distinctY), tests)

