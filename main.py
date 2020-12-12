from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color('red',)

# my_turtle.begin_fill()


def color_maker():
    r = round(random.random(), 1)
    g = round(random.random(), 1)
    b = round(random.random(), 1)
    return r, g, b


def make_shape(shape_no):
    return 360 / shape_no


for shapes in range(3, 11):
    for _ in range(shapes):
        my_turtle.forward(100)
        my_turtle.left(make_shape(shapes))
        my_turtle.pencolor(color_maker())


# my_turtle.end_fill()

# my_turtle.begin_fill()
# while True:
#     my_turtle.forward(100)
#     my_turtle.left(72)
#     if abs(my_turtle.pos()) < 1:
#         break
# my_turtle.end_fill()


# for _ in range(10):
#     my_turtle.forward(10)
#     my_turtle.pu()
#     my_turtle.forward(10)
#     my_turtle.pd()


my_screen = Screen()
my_screen.exitonclick()

