#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from tkinter import *


class Converter:

    def __init__(self):
        self.tag = 1
        self.window = Tk()
        self.window.title('Mile to Km Converter')
        self.window.config(padx=20, pady=20)

        self.entry = Entry(width=5)
        self.entry.grid(column=1, row=0)

        self.m_label = Label(text='Miles')
        self.m_label.grid(column=2, row=0)

        self.i_label = Label(text='is equal to')
        self.i_label.grid(column=0, row=1)

        self.n_label = Label(text='0')
        self.n_label.grid(column=1, row=1)

        self.k_label = Label(text='Km')
        self.k_label.grid(column=2, row=1)

        self.button = Button(text='calculate', command=self.calculate)
        self.button.grid(column=1, row=2)

        self.switch_button = Button(text='↕️', command=self.switch_clicked)
        self.switch_button.grid(column=3, row=1)

        self.window.mainloop()

    def calculate(self):
        if self.tag == 1:
            self.mile_to_km()
        else:
            self.km_to_mile()

    def switch_clicked(self):
        self.tag *= -1
        if self.tag == 1:
            self.m_label.config(text='Miles')
            self.k_label.config(text='Km')
        else:
            self.m_label.config(text='Km')
            self.k_label.config(text='Miles')
        self.calculate()

    def km_to_mile(self):
        kms = float(self.entry.get())
        miles = round(kms / 1.609, 2)
        self.n_label.config(text=miles)

    def mile_to_km(self):
        miles = float(self.entry.get())
        kms = round(1.609 * miles, 2)
        self.n_label.config(text=kms)


if __name__ == '__main__':
    converter = Converter()
