#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import tkinter as tk
from tkinter import messagebox
import string
import time


class DisappearingTextWritingApp:

    def __init__(self, master):
        self.master = master
        self.master.title('The Most Dangerous Writing App')
        self.time_limit = 5  # second
        self.word_number = 0
        self.status = 0  # 0 not start 1 ongoing 2 end
        self.last_type_time = time.time()

        # init layout
        self.text_input = tk.Text(width=50, height=20)
        self.text_input.pack(pady=20)

        self.label = tk.Label(
            self.master,
            text=self.generate_text(),
            font=(
                "Arial",
                25),
            wraplength=500,
            justify="center")
        self.label.pack()

        self.input_bind()  # bind events

    def update_label(self):
        self.label.config(
            text=self.generate_text())
        self.check_last_typing()

    def generate_text(self):
        self.word_number = self.count_num()
        text = f'You have typed {self.word_number} words. ' \
            f'All content will disappear if you stop typing for {self.time_limit} seconds.'
        return text

    def count_num(self):
        text = self.text_input.get('1.0', 'end').strip()
        return 0 if len(text) == 0 else len(text.split(' '))

    def counting_down(self):
        self.master.after(1000, self.counting_down)
        self.update_label()

    def update_last_typing_time(self):
        self.last_type_time = time.time()

    def input_bind(self):
        for i in string.ascii_letters:
            self.text_input.bind(
                str(i), lambda event: self.counting_down(), add='+')
            self.text_input.bind(
                str(i), lambda event: self.update_status(1), add='+')
            self.text_input.bind(
                str(i), lambda event: self.update_last_typing_time(), add='+')
            self.text_input.bind(
                str(i), lambda event: self.check_last_typing(), add='+')

    def clear_input_text(self):
        self.text_input.delete('1.0', 'end')

    def update_status(self, status):
        self.status = status
        for i in string.ascii_letters:
            self.text_input.unbind_all(str(i))

    def restart(self):
        self.word_number = 0
        self.status = 0  # 0 not start 1 ongoing 2 end

    def check_last_typing(self):
        if time.time() - self.last_type_time >= self.time_limit and self.status == 1:
            self.clear_input_text()
            self.status = 2
            answer = messagebox.askokcancel(  # get user choice
                message='Time Over! Do you want to restart?')
            if answer:  # continue
                self.restart()
            else:  # quit
                self.master.destroy()


root = tk.Tk()
root.geometry('600x400')
disappearing_text_writing_app = DisappearingTextWritingApp(root)
root.mainloop()
