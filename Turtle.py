import turtle
import time
bob = turtle.Turtle()
bob.color('green', 'yellow')
for i in range(4):
    bob.begin_fill() 
    for i in range(4): 
        bob.forward(100)
        bob.left(90)
    bob.end_fill()

    bob.penup()
    bob.forward(30)
    bob.pendown()
turtle.done()
