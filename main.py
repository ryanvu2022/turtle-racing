from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, blue, green, purple): ").lower()
colors = ["red", "orange", "yellow", "blue", "green", "purple"]

all_turtles = []

y_position = -125
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.resizemode("user")
    new_turtle.shapesize(1.5, 1.5, 1.5)
    new_turtle.goto(-230, y_position)
    all_turtles.append(new_turtle)
    y_position += 50

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_move = random.randint(0, 10)
        turtle.forward(random_move)


screen.exitonclick()
