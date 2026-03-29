import cython

class Sprite:
    def __init__(pos, icon):
        self.x, self.y = pos
        self.icon = icon

class direction:
    right = 1
    up = 2
    left = 3
    down = 4

if __name__ == "__main__":
    import unittest

    class testSprite(unittest.TestCase):
        def setUp(self):
            ...

        def test_turn(self):
            print(direction.right direction.left) 

    unittest.main()