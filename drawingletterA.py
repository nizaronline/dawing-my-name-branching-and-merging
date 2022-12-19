#drawing the letter A

# i am creating a function called letterA that draws the letter A
# i will use this file as a module


# importing the module turtle and all of its methods
from turtle import *


def letterA ():
    ### the purpose of this function is to draw the fourth letter, A, which contains three parts:

        # drawing the letter A, first part

    goto(120.00,0) # moving the turtle next to the right bottom edge of the letter Z
    setheading(0)   # needed to make calculations of the angle easier
    right (25)
    begin_fill()
    pendown()
    forward(330)
    print(position())  # required to get the position for further drawings
    circle(10,180)
    print(position())  
    forward(330)
    circle(10,180)
    end_fill()
    penup()


        #drawing the letter A, second part

    goto(247.92,299.10) # moving the turtle next to the top edge
    setheading(0)   # needed to make calculations of the angle easier
    right(155)
    begin_fill()
    pendown()
    forward(330)
    circle(10,180)
    forward(330)
    circle(10,180)
    end_fill()
    penup()


        # drawing the letter A, third part

    goto(170,150) # moving the turtle to the near field next to the top of the letter I
    setheading(0)
    right(90)
    begin_fill()
    pendown()
    forward(175)
    circle(10,180)
    forward(175)
    circle(10,180)
    end_fill()
    penup()
