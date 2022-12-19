#drawing the letter R

# i am creating a function called letterA that draws the letter R
# i will use this file as a module


# importing the module turtle and all of its methods
from turtle import *


def letterR ():
    ### the purpose of this function is to draw the fifth and the last letter, R, which contains three parts:

        # drawing the letter R, first part

    goto(440,0) # moving the turtle to the bottom  part, next to the edge, so it starts drawing from there
    setheading(0)  # change the direction of the turtle's head, to make the head towards north
    begin_fill()
    pendown()
    forward(310)
    circle(10,180)
    forward(310)
    circle(10,180)
    end_fill()
    penup()

        # drawing the letter R, second part

    goto(440,310) 
    setheading(0)
    begin_fill()
    pendown()
    backward(20)
    right (90)
    circle(-60,180)
    setheading(0)
    backward(20)
    right (90)
    circle(82.5,180)
    end_fill()
    penup()

        # drawing the letter R, third part

    goto(430.00,160.00) 
    setheading(0)  
    right (155)
    begin_fill()
    pendown()
    forward(180)
    circle(10,180)
    forward(180)
    circle(10,180)
    end_fill()
    penup()



