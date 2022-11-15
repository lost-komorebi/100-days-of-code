#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from brick_manager import BrickManager


screen = Screen()
screen.setup(1000, 600)
screen.title('Breakout Game')
screen.bgcolor('black')
screen.tracer(0)

paddle = Paddle()
scoreboard = ScoreBoard()
brick_manager = BrickManager()
ball = Ball()
ball.move()

is_game_on = True
chance = 3  # user has 3 times


def restart():
    global is_game_on
    global chance
    is_game_on = True
    chance = 3
    scoreboard.reset()
    ball.reset()
    brick_manager.reset()


screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')
screen.onkey(restart, 'space')


while is_game_on:
    screen.update()
    ball.move()

    # detect ball and wall(left and right) collision
    if ball.xcor() >= 490 or ball.xcor() <= -490:
        ball.change_x()

    # detect ball and paddle collision
    if ball.is_collision(paddle):
        ball.change_y()

    # detect ball and bricks collision
    for brick in brick_manager.bricks:
        if ball.is_collision(brick):
            # move brick out of screen, don't use hideturtle
            brick.goto(1000, 1000)
            ball.change_y()
            scoreboard.update_score()
            brick_manager.bricks_number -= 1

    # detect ball and wall(up and down) collision
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.goto(0, 0)
        chance -= 1

    if chance == 0:
        is_game_on = False
        scoreboard.game_over()

    if brick_manager.bricks_number == 0:
        is_game_on = False
        scoreboard.win()


screen.exitonclick()
