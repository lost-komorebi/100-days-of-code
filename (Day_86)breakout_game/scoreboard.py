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
        self.write_board()

    def write_board(self):
        self.clear()
        self.write(self.score, align='center', font=(
            'Arial',
            40,
            'normal'))

    def update_score(self):
        self.score += 1
        self.write_board()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=(
            'Arial',
            40,
            'normal'))

    def win(self):
        self.goto(0, 0)
        self.write('You are winner!', align='center', font=(
            'Arial',
            40,
            'normal'))
