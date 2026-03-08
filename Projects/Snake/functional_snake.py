# Functional Snake 0 ☠️

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
"""

def board(w=37, h=33):
    return ["·" * w] * h
    
def sprite(x, y):
    return (x, y)
    
class Sprite:
    def __init__(self, x, y):
        self.pos = (x, y)
    
    def walk(self, direction):
        self.pos = self + direction
    
    def __add__(self, pair):
        x = self.pos[0] + pair[0]
        y = self.pos[1] + pair[1]
        return (x, y)