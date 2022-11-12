#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle
ALIGNMENT = 'center'
FONT = (
    'Arial',
    20,
    'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color('white')
        self.penup()
        self.setposition(0, 275)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False,
                   align=ALIGNMENT,
                   font=FONT)

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            False,
            align=ALIGNMENT,
            font=FONT)
