#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.shape('square')
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(450, 250)
        self.write_board(self.score, 0)

    def write_board(self, arg, w_type):
        if w_type == 0:
            self.clear()
        self.write(arg, align='center', font=(
            'Arial',
            40,
            'normal'))

    def update_score(self):
        self.score += 1
        self.write_board(self.score, 0)

    def game_over(self):
        arg = '             GAME OVER \n PRESS SPACE TO RESTART'
        self.goto(0, 0)
        self.write_board(arg, 1)

    def win(self):
        arg = '         You are winner! \n PRESS SPACE TO RESTART'
        self.goto(0, 0)
        self.write_board(arg, 1)

    def reset(self):
        self.goto(450, 250)
        self.score = 0
        self.write_board(self.score, 0)

