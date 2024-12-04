import random
from turtle import Turtle, Screen
Race = False
s = Screen()
s.setup(width = 500, height = 400)
bet = s.textinput(title = "make your bet", prompt = "which turtle which win ? enter color(red/yellow/orange/blue/violet): ")
X = -230
Y = -100
colors = ["red", "orange", "yellow", "blue", "violet"]
turtles = []
for i in range(5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x = X, y = -100 + 50 * i)
    turtles.append(t)
if bet:
    Race = True
while Race:
    for turtle in turtles:
        if turtle.xcor()>= 230:
            Race = False
            winning = turtle.pencolor()
            if winning == bet:
                print(f"you have won the bet on {winning} turtle the {winning} is the winner")
            else:
                print(f"you lose {winning} turtle is winner")
        distance = random.randint(0, 10)
        turtle.forward(distance)
s.exitonclick()
