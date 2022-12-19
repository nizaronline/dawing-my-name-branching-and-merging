# drawing the letter N

# i am creating a function called letterN that draws the letter N
# i will use this file as a module

# importing the module turtle and all of its methods
import turtle as t

#defining the screen as an object
screen=t.Screen()
screen.bgcolor("white")
screen.title("Writing My Name, another edition")

# defining the turtle as the object which makes the drawing
t.color("black")
t.speed(0)
t.mode("logo") # to make the turtle head to the north, and the postitve angles for counterclockwise rotation
t.penup()
t.hideturtle() # it is optinal, just to hide the object to make better animation


def letterN ():
    ### the purpose of this function is to draw the first letter, N, which contains three parts:

       # drawing the letter N, first part

    t.goto(-300,0) # moving the turtle to a start point, located at the left bottom region of the screen
    t.pendown() # order the turtle to trace
    t.begin_fill() # filling the future drawing after closing lines
    t.forward (300) # tracing a straight vertical line from the botton to to top
    circle(10,180) #  drawing half a circle to the left
    forward(300) #tracing back a straight vertical line from the top  to to bottom
    circle(10,180) # drawing the half of circle in order to close the drawing
    end_fill() #filling the drawing after the lines have been closed
    penup() # ordering the turtle to not to draw


        # drawing the letter N, second part

    goto(-315,300) # moving the turtle to th top part so it starts drawing from there
    begin_fill()
    right(157.5)    # in this case, i need to change the dircection of the turtle's head,
                    #setting the angle at -45° on the x axis
                    # so it can draw the diagonal from top left corner to botton right corner.
    pendown()
    forward(330)
    print(position())   # i need this command to get the exact position of the turtle at the end of the execution of the previous command
                        # this helps me to set the right position or angle for next orders.
    print(heading())    #get the angle of the head
    circle(10,180)
    print(position())
    print(heading())
    forward(330)
    circle(10,180)
    end_fill()
    penup()



        # drawing the letter N, third part

    goto(-170,0) # moving the turtle to the bottom  part so it starts drawing from there
    setheading(0)  # change the direction of the turtle's head, to make the head towards north
    begin_fill()
    pendown()
    forward(300)
    circle(10,180)
    forward(300)
    circle(10,180)
    end_fill()
    penup()




