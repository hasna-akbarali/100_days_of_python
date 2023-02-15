""" Moving the turtle in reverse manner """
import turtle

# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle("turtle")
# timmy_the_turtle.color("green")
#
#
# def change():
#     if timmy_the_turtle.isdown():
#         timmy_the_turtle.penup()
#     else:
#         timmy_the_turtle.pendown()
#
# times = 3
#
# for i in range(times):
#     timmy_the_turtle.forward(10)
#     change()
#
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(10)
# timmy_the_turtle.right(90)
#
# for i in range(30):
#      timmy_the_turtle.forward(10)
#      change()
#
#     # timmy_the_turtle.right(90)
#     # timmy_the_turtle.forward(10)
#     # timmy_the_turtle.backward(10)

# # https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
# # dark_sea_gren = (143,188,143)
# # timmy_the_turtle.pencolor(143,188,143)
# my_screen = Screen()
# my_screen.exitonclick()

'''Draw triangle, square, pentagon, hexagon, octagon, nanogon etc..'''
# from turtle import Turtle, Screen
# import random
#
# tim = Turtle("turtle")
# tim.width(10)
# times = 3
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "navy", "SlateGray",
#            "Firebrick", "indigo", "DarkMagenta"]
#
# while times < 11:
#     for i in range(times):
#         tim.forward(100)
#         tim.right(360 / times)
#     tim.color(random.choice(colours))
#     times = times + 1
#
# my_screen = Screen()
# my_screen.exitonclick()

'''Draw a random path with color changes in every step'''
from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle("arrow")
tim.width(10)
tim.speed('fastest')
turtle.colormode(255)
colors = colorgram.extract('damien.jpeg', 6)


def color_change():
    n = random.randint(0, 5)
    r = colors[n].rgb.r
    g = colors[n].rgb.g
    b = colors[n].rgb.b
    tim.color(r, g, b)


directions = [0, 90, 180, 270]

for i in range(300):
    tim.forward(20)
    tim.setheading(random.choice(directions))
    color_change()

my_screen = Screen()
my_screen.exitonclick()

'''Draw a spirograph of randomized colors'''
# from turtle import Turtle, Screen
# import colorgram
# import random
#
# tim = Turtle("arrow")
# tim.speed('fastest')
# turtle.colormode(255)
# colors = colorgram.extract('spot.jpeg', 6)
#
#
# def color_change():
#     n = random.randint(0, 5)
#     r = colors[n].rgb.r
#     g = colors[n].rgb.g
#     b = colors[n].rgb.b
#     tim.color(r, g, b)
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(360 // size_of_gap):
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#         color_change()
#
#
# draw_spirograph(1)
# my_screen = Screen()
# my_screen.exitonclick()
