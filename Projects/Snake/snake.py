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

class Board:
    def __init__(self, w=40, h=40):
        self.w, self.h = w, h
        self.board = self.new_board()
        self.snake = Snake((2, 0), (1, 0))
        self.food = ...
        self.keyPressed = ""
        
    def new_board(self):
        return [["."] * self.w] * self.h
        
    def render(self):
        # Performance: use strings for empty lines, and lists for used ones.
        # if INDEX out of range:
        #   Game over or reappear in the opposite side
        
        # Get a new board, so the symbols can be drawn
        self.board = self.new_board()
        for sprite in self.snake.body:
            x, y = sprite.pos
            row = self.board[y].copy()
            row[x] = "@"
            self.board[y] = row
            sprite.direction = direction.right


    def tick(self):
        """Update the snake recursively.
        Verify if SNAKE HEAD and FOOD
        are touching."""
        if self.snake.isTouchingFood(self.food):
            #self.snake.grow()
            self.food.teleport()
            
        self.snake.walk()
        self.render()
        
    def mainloop(self):
        print(a)
        while True:
            time.sleep(0.2)
            print("=" * a.w)
            # Use async/subroutine, so the game doesn't wait for the key
            
            # Listen to Input
            self.keyPressed = get_input()
            self.tick()
            print(self)
        
    def __str__(self):
        "PERFORMANCE find a faster way."
        board = []
        for row in self.board:
            board.append("".join(row))
        return "\n".join(board)

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
    up = (0, 1)
    down = (0, -1)
    
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

def get_input() -> str:
    filedescriptors = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    key = sys.stdin.read(1)[0]
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
    
    return key

import time
import random
a = Board(w=37, h=16)
a.mainloop()