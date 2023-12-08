import unittest
import random
from vector2 import Vector2

class Vector2Test(unittest.TestCase):
    def test_init_str(self):
        x = random.randrange(1,100)
        y = random.randrange(1,100)
        v = Vector2(x,y)

        self.assertEqual(f"{x}; {y}",v.__str__())

    def test_init_properties(self):
        x = random.randrange(1,100)
        y = random.randrange(1,100)
        v = Vector2(x,y)
        self.assertEqual(x, v.x)
        self.assertEqual(y, v.y)

    def test_eq_same(self):
        x = random.randrange(1,100)
        y = random.randrange(1,100)
        v1 = Vector2(x,y)
        v2 = Vector2(x,y)
        self.assertTrue(v1==v2)

    def test_eq_not_same(self):
        x = random.randrange(1,100)
        y = random.randrange(1,100)
        v1 = Vector2(x,y)
        v2 = Vector2(x+1,y)
        self.assertFalse(v1==v2)

    def test_add(self):
        x = random.randrange(1,100)
        y = random.randrange(1,100)
        v1 = Vector2(x,y)
        v2 = Vector2(-x, -y)
        self.assertTrue(v1+v2==Vector2(0,0))
        self.assertTrue(v1+v1==Vector2(2*x,2*y))

