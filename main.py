import turtle

from colorgram import extract
from random import randint, choice
from turtle import Turtle, Screen

# colors = extract("hirst_spot.jpg", 30)
# print(colors)
# first_color = colors[0]
# print(first_color)
# rgb = first_color.rgb
# print(rgb)
# red = rgb[0]
# print(red)
# roy = rgb.r
# goy = rgb.g
# boy = rgb.b
# print(roy)
# color_list = []
# col_list = (roy, goy, boy)

# for i in range(len(colors) - 1):
#     color_list.append(colors[i].rgb)
# print(color_list)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(new_color)
# print(rgb_color)
colour_list = [(84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56),
               (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246),
               (35, 34, 253),
               (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (39, 249, 42),
               (85, 249, 253),
               (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249),
               (208, 118, 26),
               (253, 7, 4), (248, 6, 19)]

tim = Turtle()
turtle.colormode(255)

tim.hideturtle()
tim.speed(1000)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


def start():
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, choice(colour_list))
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


start()
# for i in range(4):
#     start()
#     tim.setheading(header[i])


screen = Screen()
screen.exitonclick()
