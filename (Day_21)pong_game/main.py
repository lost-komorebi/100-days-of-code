#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)


r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with up wall and down wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.xcor() >= 360 and ball.distance(r_paddle) < 60) or (
            ball.xcor() <= - 360 and ball.distance(l_paddle) < 60):
        ball.bounce_x(1)

    # detect collision with right wall and left wall
    if ball.xcor() >= 400:
        ball.miss()
        scoreboard.add_l_score()
    if ball.xcor() <= -400:
        ball.miss()
        scoreboard.add_r_score()

screen.exitonclick()
