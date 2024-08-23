from turtle import *

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

def draw_polygon(side,length):
    angle = 360/side
    for num in range(side):
        timmy_the_turtle.forward(length)
        timmy_the_turtle.right(angle)

for _ in range(3,11):
    draw_polygon(_,80)












screen = Screen()
screen.exitonclick()