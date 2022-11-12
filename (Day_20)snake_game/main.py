#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(620, 620)
screen.title('Snake game')
screen.bgcolor('black')
screen.tracer(0)  # Turn off animation

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


is_game_on = True
while is_game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() >= 305 or snake.head.xcor() <= - \
            305 or snake.head.ycor() >= 305 or snake.head.ycor() <= -305:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with snake tail
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) <= 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
