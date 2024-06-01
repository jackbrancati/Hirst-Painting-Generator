import colorgram
import turtle as t
from turtle import Screen
import random

# colors = colorgram.extract('image.jpeg', 50)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]
t.colormode(255)
todd = t.Turtle()

t.setup(1000, 600, 200)
todd.teleport(-300, -200)
todd.speed("fastest")
todd.hideturtle()
def draw_circle():
    todd.dot(20)

print(type(random.choice(color_list)))
print(random.choice(color_list))

def dots_x_axis():
    for x in range(10):
        todd.color(random.choice(color_list))
        draw_circle()
        todd.penup()
        todd.forward(50)


def last_dot_and_next_line():
    draw_circle()
    todd.left(90)
    todd.forward(50)
    todd.left(90)
    todd.forward(50 * 10)
    todd.left(180)

for y in range(112):
    dots_x_axis()
    last_dot_and_next_line()

screen = Screen()
screen.exitonclick()



