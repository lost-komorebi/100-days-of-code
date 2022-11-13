#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 250)
        self.write(
            self.r_score, False,
            align='center',
            font=(
                'Arial',
                40,
                'normal'))
        self.goto(-100, 250)
        self.write(
            self.l_score,
            False,
            align='center',
            font=(
                'Arial',
                40,
                'normal'))

    def add_l_score(self):
        self.l_score += 1
        self.update_score()

    def add_r_score(self):
        self.r_score += 1
        self.update_score()
