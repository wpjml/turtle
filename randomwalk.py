import turtle
import random

t = turtle.Turtle()

angle = [90,180,270,360]
turtle.colormode(255)
t.width(5)
t.speed("fastest")

for _ in range(2000):
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    t.pencolor(r,b,g)
    t.forward(20)
    t.right(random.choice(angle))


