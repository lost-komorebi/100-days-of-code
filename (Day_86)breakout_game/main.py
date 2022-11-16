#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from brick_manager import BrickManager


class Game:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(1000, 600)
        self.screen.title('Breakout Game')
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.is_game_on = True
        self.chance = 3  # user has 3 times
        self.paddle = Paddle()
        self.scoreboard = ScoreBoard()
        self.brick_manager = BrickManager()
        self.ball = Ball()
        self.ball.move()
        self.check_events()

    def restart(self):
        self.is_game_on = True
        self.chance = 3
        self.scoreboard.reset()
        self.ball.reset()
        self.paddle.reset()
        self.brick_manager.reset()
        self.run()

    def check_events(self):
        self.screen.listen()
        self.screen.onkey(self.paddle.move_left, 'Left')
        self.screen.onkey(self.paddle.move_right, 'Right')
        self.screen.onkey(self.restart, 'space')

    def run(self):
        while self.is_game_on:
            self.screen.update()
            self.ball.move()

            # detect ball and wall(left and right) collision
            if self.ball.xcor() >= 490 or self.ball.xcor() <= -490:
                self.ball.change_x()

            # detect ball and paddle collision
            if self.ball.is_collision(self.paddle):
                self.ball.change_y()

            # detect ball and bricks collision
            for brick in self.brick_manager.bricks:
                if self.ball.is_collision(brick):
                    # move brick out of screen, don't use hideturtle
                    brick.goto(1000, 1000)
                    self.ball.change_y()
                    self.scoreboard.update_score()
                    self.brick_manager.bricks_number -= 1

            # detect ball and wall(up and down) collision
            if self.ball.ycor() >= 280 or self.ball.ycor() <= -280:
                self.ball.goto(0, 0)
                self.chance -= 1

            if self.chance == 0:
                self.is_game_on = False
                self.scoreboard.game_over()

            if self.brick_manager.bricks_number == 0:
                self.is_game_on = False
                self.scoreboard.win()

        self.screen.exitonclick()


game = Game()
game.run()
