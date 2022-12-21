# this program is intended to draw my name using the language Python and the module turtle
# this version is used with branching and merging
# every branch consists in drawing only one letter,
# the master branch is for screen and object
# every branch is in a specific file

## a different approach is made : a fucntion is written in anoher file
##which consists in a module to be imported.


# importing the module turtle and all of its methods
from turtle import *

# importing the module letterN which contains the related function to draw the corresponding letter
from drawingletterN import letterN
# importing the module letterI which contains the related function to draw the corresponding letter
from drawingletterI import letterI
# importing the module letterZ which contains the related function to draw the corresponding letter
from drawingletterZ import letterZ
# importing the module letterA which contains the related function to draw the corresponding letter
from drawingletterA import letterA
# importing the module letterR which contains the related function to draw the corresponding letter
from drawingletterR import letterR

#defining the screen as an object
screen=Screen()
screen.bgcolor("white")
screen.title("Writing My Name, another edition")

# defining the turtle as the object which makes the drawing
color("black")
speed(0)
mode("logo") # to make the turtle head to the north, and the postitve angles for counterclockwise rotation
penup()
hideturtle() # it is optinal, just to hide the object to make better animation


# drawing all the letters, one by one, by calling the corresponding function :

letterN()
letterI()
letterZ()
letterA()
letterR()





