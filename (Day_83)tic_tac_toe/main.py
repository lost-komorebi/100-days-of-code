#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


import re


class TicTacToe:
    def __init__(self):
        self.ttt = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        print('Welcome to Tic Tac Toe')
        self.player = 1  # default player
        self.status = 0  # default status is start
        self.display()

    def display(self):
        for index, i in enumerate(self.ttt):
            print('|'.join(i))
            if index != 2:
                print('-----')

    def check_win(self):
        for i in range(3):
            if self.ttt[i][0] == self.ttt[i][1] == self.ttt[i][2] != ' ':  # check transversely
                self.winning_notice()
            elif self.ttt[0][i] == self.ttt[1][i] == self.ttt[2][i] != ' ':  # check vertically
                self.winning_notice()
        if self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2] != ' ':  # check diagonal
            self.winning_notice()
        if self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0] != ' ':  # check diagonal
            self.winning_notice()

    def update_ttt(self, x, y):
        if self.player == 1:
            self.ttt[x][y] = 'X'
        else:
            self.ttt[x][y] = 'O'
        self.display()
        self.check_win()
        self.player *= -1

    def get_user_input(self):
        if self.status == 0:
            if self.player == 1:
                print("Now is play1's(X) turn")
                user_input = input('Please enter(row,column, eg: 1,2):')
            else:
                print("Now is play2's(O) turn")
                user_input = input('Please enter(row,column eg: 1,2):')
            m = re.match(r'([1-3]),([1-3])', user_input)  # validate user_input
            if m:
                if self.ttt[int(m.group(1)) -
                            1][int(m.group(2)) -
                               1] in ('X', '0'):
                    print('You can not mark this place!')
                    self.get_user_input()
                self.update_ttt(int(m.group(1)) - 1, int(m.group(2)) - 1)
            else:
                print('Invalid Input!')
                self.get_user_input()
        else:
            user_input = input("Enter 'yes' to start a new game, \n"
                               "Enter any other word to quit:")
            if user_input.lower() == 'yes':
                self.__init__()  # reset
            else:
                quit()

    def winning_notice(self):
        self.status = 1
        if self.player == 1:
            print('Player1 is winner!')
        else:
            print('Player2 is winner!')

    def main(self):
        while True:
            self.get_user_input()


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.main()

