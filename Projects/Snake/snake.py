# Snake 0 ☠️

"""
# InThis Terminal:
# A LINE HAS 37 CHARS.
# A SCREEN FITS 33 LINES

The BOARD matrix is made of 33 lines,
each one is a string of 37 chars.

Implement "walking" to an object.

Each sprite will be a tuple in a list
of sprites SNAKE.
(x, y)

it should walk:
    At every TICK, add DIRECTION to 
    the SPRITE tuple.

[x] At every tick, the board should be
re-rendered, effectively printing the
BOARD matrix.

To create a NEW snake tail block:
    Get the tail.pos
    get the tail.direction
    the new pos is = tpos - tdir
    # Because it is one block behind :)

2 player game ☠☠☠
"""

"""
TODO:
List based tail direction changing.
Keyboard movement.
Food mechanics. (Food array for various)
Game over.
"""

"""
Settings

# Change time.sleep inside board.mainloop()
board.tickSpeed = 0.2s
"""

"""
Ideas

# Multiplayer
Add an array for board.snakes
Multiple keyListeners at each second
"""



class Snake:
    def __init__(self, *body):
        self.body = list(map(Sprite.tuple_init, body))
        self.turning = [(0, 0)] * len(body)
    
    def grow(self):
        # tail = self.body[-1]
        # Add a new sprite to the tail
        self.body.append(
            Sprite.tuple_init(self.body[-1].behind())
            )

    def walk(self):
        for sprite in self.body:
            sprite.walk()
            
    def turn(self, direction):
        self.turning.insert(0, direction)
        l = len(self.body)
        for i in range(l):
            self.body[i].direction = self.turning[i] 
        
    def isTouchingFood(self, food):
        return self.body[0].pos == food.pos
            
    def isHittingWall(self, boardSize):
        """Return true if walking into wall.
        Or walking into iself."""
        ...
        
    def update_head_tail(self):
        ...
        #self.head = self.body[1]
        #self.tail = self.body[-1]
        
    def __str__(self):
        return str([b.pos for b in self.body])

class Food():
    ...
    
    def teleport():
        ...

class direction:
    right = (1, 0)
    left = (-1, 0)
    
keys = {
    "d": direction.right,
    "a": direction.left
}    

class Sprite:
    """SpriteAPI: The basic building
    blocks for py gaming."""

    def __init__(self, x, y):
        self.pos = (x, y)
        self.direction = direction.right
    
    def tuple_init(pos):
        return Sprite(pos[0], pos[1])
        
    def walk(self):    
        self.pos = self.add(self.direction)
    
    def behind(self):
        """Get the coords of the block behind this sprite, based on it's direction of movement."""
        return self.sub(self.direction)
    
    # def turn(self, d):
    #    self.direction = direction.d

    def add(self, pair):
        "Add an ordenated Pair to another"
        x = self.pos[0] + pair[0] # Ax + Bx
        y = self.pos[1] + pair[1] # Ay + By
        return (x, y)
        
    def sub(self, pair):
        "Subtract an ordenated Pair from another"
        x = self.pos[0] - pair[0] # Ax - Bx
        y = self.pos[1] - pair[1] # Ay - By
        return (x, y)

def findFreeRandomCoords(boardSize, sprites):
    "Only use FREE squares."
    ...

import termios
import tty
import sys

from instant_input import get_input

import time
import random

from lib.board import Board
a = Board(size=(37, 16))
a.mainloop()