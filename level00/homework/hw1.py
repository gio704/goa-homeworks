from turtle import *


#we wont to paint a house

#step 1: draw a square
speed(30)
width(7)
color("blue")
forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
begin_fill()
begin_fill()
color("green")
left(30)
forward(70)
left(90)
forward(50)
left(90)
forward(70)
left(90)
forward(50)
right(180)
forward(200)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()








exitonclick ()