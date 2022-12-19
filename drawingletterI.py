# drawing the letter I

# i am creating a function called letterN that draws the letter I
# i will use this file as a module


# importing the module turtle and all of its methods
from turtle import *


def letterI ():
    ### the purpose of this function is to draw the seond letter, I, which contains three parts:

       # drawing the letter I, first part
    
    goto (-130,0) # moving the turtle to the near field next the letter N
    setheading(0)  # change the direction of the turtle's head, to make the head towards north
    begin_fill()
    pendown()
    forward(300)
    circle(10,180)
    forward(300)
    circle(10,180)
    end_fill()
    penup()


