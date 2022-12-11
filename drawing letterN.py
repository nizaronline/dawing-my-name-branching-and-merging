# drawing the letter N, first part

goto (-300,0) # moving the turtle to a start point, located at the left bottom region of the screen
pendown() # order the turtle to trace
begin_fill() # filling the future drawing after closing lines
forward (300) # tracing a straight vertical line from the botton to to top
circle(10,180) #  drawing half a circle to the left
forward(300) #tracing back a straight vertical line from the top  to to bottom
circle(10,180) # drawing the half of circle in order to close the drawing
end_fill() #filling the drawing after the lines have been closed
penup() # ordering the turtle to not to draw
