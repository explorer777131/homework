from turtle import *
width(7)
speed(30)
color("dark red")

forward (200)
left (90)

forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#door
forward(70)

color("violet")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown
color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)

end_fill()

#windows
penup()
goto(30, 160)
pendown()

color("blue")
begin_fill()
left(30)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()






exitonclick()