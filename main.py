from painting import colors_list
import turtle as t
from turtle import Turtle, Screen
import random

screen = Screen()
t.colormode(255)
tim = Turtle()

# Setting up initial position
tim.hideturtle()
tim.penup()
tim.speed('fastest')

# Main Parameters / User Defined
STEP_SIZE = int(input("Define the step size: "))
DOT_SIZE = int(input("Define the dot size: "))

if STEP_SIZE < DOT_SIZE:
    DOT_SIZE = STEP_SIZE

# defining starting position
start_height = -400
start_width = -400
tim.goto(start_width, start_height)

# computing the number of dots acceptable
density_dots = int(((abs(start_height)+abs(start_width))/STEP_SIZE)+1)

# generating the artwork
for row in range(density_dots):
    for column in range(density_dots):
        color = random.randint(0,9)
        tim.dot(DOT_SIZE, (colors_list[color]['r'], colors_list[color]['g'], colors_list[color]['b']))
        tim.forward(STEP_SIZE)
    start_height += STEP_SIZE
    tim.goto(start_width, start_height)

# to leave the GUI
screen.exitonclick()