import turtle as t
from turtle import Turtle, Screen
import random as rn


# Competing turtles
# I opted for multiple instances compared to Angela
tim = Turtle()
tim.shape("turtle")
tim.color("red")

tom = Turtle()
tom.shape("turtle")
tom.color("blue")

sam = Turtle()
sam.shape("turtle")
sam.color("green")

sim = Turtle()
sim.shape("turtle")
sim.color("yellow")

som = Turtle()
som.shape("turtle")
som.color("purple")

# Screen initialization
screen = Screen()
width = 500
height = 400
screen.setup(width, height)

# Make a bet

user_bet = screen.textinput(title= "Make a bet!", prompt = "Select the color of the turtle you are betting on: ").lower()

tim.penup()
tim.goto(-200, 80)
tom.penup()
tom.goto(-200, 40)
sam.penup()
sam.goto(-200, 0)
sim.penup()
sim.goto(-200, -40)
som.penup()
som.goto(-200, -80)

def race():
    while check_positions():
            tim.forward(rn.randint(10,30))
            tom.forward(rn.randint(10,30))
            sim.forward(rn.randint(10,30))
            sam.forward(rn.randint(10,30))
            som.forward(rn.randint(10,30))

def check_positions():
    positions = {
         "red": tim.pos()[0], 
         "blue": tom.pos()[0], 
         "green": sam.pos()[0], 
         "yellow": sim.pos()[0], 
         "purple": som.pos()[0]
         }
    if any(x > 200 for x in positions.values()):
        winner = max(positions, key=positions.get)
        if user_bet == winner:
            print(f"Hai vinto! Ha vinto {user_bet}")
        else:
            print("Hai perso :(")
        return False
    else:
         return True

screen.listen()
screen.onkey(fun = race, key="space")

# Exit the game
screen.exitonclick()
