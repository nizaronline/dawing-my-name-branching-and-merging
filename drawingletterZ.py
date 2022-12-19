# drawing the letter Z

# i am creating a function called letterZ that draws the letter Z
# i will use this file as a module


# importing the module turtle and all of its methods
from turtle import *


def letterZ ():
    ### the purpose of this function is to draw the third letter, Z, which contains three parts:

        # drawing the letter Z, first part

    goto (-90,290) # moving the turtle to the near field next to the top of the letter I
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


        # drawing the letter Z, second part

    goto (85.00,305.00) # moving the turtle to the right edge of the first part
    setheading(0)       # needed to make calculations of the angle easier
    left(147.5)
    begin_fill()
    pendown()
    forward(350)
    circle(10,180)
    forward(350)
    circle(10,180)
    end_fill()
    penup()


        # drawing the letter Z, third part


    goto (-90.00,10) # moving the turtle to the near field next to the left bottom of the second part
    setheading(0)
    right(90)
    begin_fill()
    pendown()
    forward(175)
    circle(-10,180)
    print(position())  # required to get the position
    forward(175)
    circle(-10,180)
    end_fill()
    penup()
