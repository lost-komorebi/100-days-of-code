#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import tkinter as tk
from tkinter import messagebox
from random import choices


class TyingSpeedTest:

    def __init__(self, master):
        self.master = master
        master.title('Typing Speed Test')
        self.count = 60
        self.status = 0  # default status 0 ongoing 1 end
        self.word_index = 0  # mark the word that user is typing
        self.right_number = 0  # the correct number of user typing

        self.test_text = self.get_text()
        print(self.test_text)

        self.cpm_label = tk.Label(text='Corrected CPM: ')
        self.cpm_label.grid(column=0, row=0)

        self.cpm_text = tk.Text(width=5, height=1)
        self.cpm_text.insert('1.0', '?')
        self.cpm_text.configure(state='disabled')
        self.cpm_text.grid(column=1, row=0)

        self.wpm_label = tk.Label(text='WPM: ')
        self.wpm_label.grid(column=2, row=0)

        self.wpm_text = tk.Text(width=5, height=1)
        self.wpm_text.insert('1.0', '?')
        self.wpm_text.configure(state='disabled')
        self.wpm_text.grid(column=3, row=0)

        self.tl_label = tk.Label(text='Time left: ')
        self.tl_label.grid(column=4, row=0)

        self.tl_text = tk.Text(width=5, height=1)
        self.tl_text.insert('1.0', str(self.count))
        self.tl_text.configure(state='disabled')
        self.tl_text.grid(column=5, row=0)

        self.restart_button = tk.Button(
            text='Restart', command=self.restart)
        self.restart_button.grid(column=6, row=0)

        self.text = tk.Text(font=('', 20), height=3, width=50, wrap='word')
        self.update_text()
        self.text.grid(column=0, row=1, columnspan=7, padx=30, pady=30)

        # configure the foreground of the text
        self.text.tag_config('fore', foreground='blue')
        # configure the background of the text
        self.text.tag_config('back', background='pink')
        # configure the alignment of the text
        self.text.tag_config('center', justify='center')
        self.text.tag_add('center', '1.0', 'end')  # add tag in specify text

        self.entry = tk.Entry(width=45)
        self.entry.focus_set()
        self.entry.grid(column=0, row=2, columnspan=7, pady=(0, 30))

        self.bindings()
        self.run()

    def get_text(self):
        with open('word_list.txt', 'r') as f:
            word_list = f.read().split('•')
        return ' '.join(choices(word_list, k=18))

    def count_down(self):
        self.entry.unbind('<Key>')
        if self.count > -1:
            self.tl_text.configure(state='normal')
            self.tl_text.delete('1.0', tk.END)
            self.tl_text.insert('1.0', str(self.count))
            self.tl_text.configure(state='disabled')
            self.master.after(1000, self.count_down)
            self.count -= 1
        else:
            number = self.cal_speed()
            messagebox.showinfo(message=f'Your score: {number} WPM ')

    def cal_speed(self):
        if self.test_text.split(' ')[
                self.word_index].strip() == self.entry.get().strip():
            self.right_number += 1

        return self.right_number

    def add_foreground(self, start, end):
        self.text.tag_add('fore', start, end)

    def remove_foreground(self, start, end):
        self.text.tag_remove("fore", start, end)

    def add_background(self, start, end):
        self.text.tag_add('back', start, end)

    def remove_background(self, start, end):
        self.text.tag_remove("back", start, end)

    def update_text(self):
        self.word_index = 0
        self.test_text = self.get_text()
        self.text.configure(state='normal')
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', self.test_text)
        self.text.configure(state='disabled')

    def run(self):

        if self.word_index >= len(self.test_text.split(' ')):
            self.update_text()
        word = self.test_text.split(' ')[
            self.word_index]  # the word user is typing
        count_var = tk.StringVar()
        self.remove_background('1.0', 'end')
        pos = self.text.search(
            word,
            '1.0',
            stopindex='end',
            count=count_var)
        self.add_background(pos, f"{pos} + {count_var.get()}c")

    def reset_entry(self):
        self.entry.delete(0, 'end')

    def bindings(self):
        self.entry.bind('<Key>', lambda event: self.count_down())
        self.entry.bind('<space>', lambda event: self.cal_speed(), add='+')
        self.entry.bind('<space>', lambda event: self.update_index(), add='+')
        self.entry.bind('<space>', lambda event: self.run(), add='+')
        self.entry.bind('<space>', lambda event: self.reset_entry(), add='+')

    def update_index(self):
        self.word_index += 1
        # print(self.word_index)

    def restart(self):
        pass


root = tk.Tk()
typing_speed_test = TyingSpeedTest(root)
root.mainloop()
