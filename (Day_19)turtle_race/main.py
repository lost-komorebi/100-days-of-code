#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
y_positions = -120
is_game_on = False

bet = screen.textinput(
    title='Turtles race bet',
    prompt='Which color will win the race?')

if bet:
    is_game_on = True


for i in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color_list[i])
    new_turtle.penup()
    y_positions += 34
    new_turtle.goto(-235, y_positions)
    turtles.append(new_turtle)


while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 215:
            is_game_on = False
            if turtle.pencolor() == bet:
                print(f"You've won! The {turtle.pencolor()} turtle is winner!")
            else:
                print(
                    f"You've lost! The {turtle.pencolor()} turtle is winner!")
        random_pace = randint(0, 10)
        turtle.forward(random_pace)


screen.exitonclick()

