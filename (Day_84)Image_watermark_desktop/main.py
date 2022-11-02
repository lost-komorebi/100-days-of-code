#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import ImageTk, Image, ImageFont, ImageDraw
import os


class ImageWaterMark:

    def __init__(self, master):
        self.master = master
        master.title("Image Watermark Desktop")
        self.upload_button = tk.Button(
            master, text='Upload', command=self.upload)
        self.upload_button.grid(column=0, row=0)
        self.canvas = tk.Canvas(width=200, height=200)  # set canvas size
        self.canvas.grid(column=0, row=1, columnspan=3)
        self.img = None
        self.img_copy = None
        self.image_on_canvas = None
        self.add_wt_success = 0  # marks whether the watermark added successfully

        self.input_label = tk.Label(master, text='Watermark:')
        self.input_label.grid(column=0, row=2)

        self.input_entry = tk.Entry(master)
        self.input_entry.grid(column=1, row=2)

        self.add_button = tk.Button(
            master,
            text='Add Watermark',
            command=self.add_watermark)
        self.add_button.grid(column=2, row=2)

        self.download_button = tk.Button(
            master, text='Download', command=self.save)
        self.download_button.grid(column=0, row=3)

    def upload(self):
        f_types = [('Jpg Files', '*.jpg'), ('Png Files', '*.png'),
                   ('Bmp Files', '*.bmp')]  # supported file
        # open file choose dialog and return the selected filename
        filename = askopenfilename(filetypes=f_types)
        img = Image.open(filename)  # return an image object
        img_resized = img.resize((200, 200))  # resize img
        self.img_copy = img_resized.copy()
        self.img_copy.filename = filename
        self.img = ImageTk.PhotoImage(img_resized)
        # the center of the img will locate at 100,100
        self.image_on_canvas = self.canvas.create_image(
            100, 100, image=self.img)

        # tkinter PhotoImage does not support jpg, so we need to use
        # PIL.ImageTk.PhotoImage
        # self.img = ImageTk.PhotoImage(file=filename)  # return an image object
        # self.canvas.create_image(100, 100, image=self.img)

    def get_watermark(self):
        if not self.img:
            messagebox.showerror(
                title='error',
                message='Please upload photo first!')
        else:
            watermark = self.input_entry.get()
            if len(watermark) == 0:
                messagebox.showerror(
                    title='error', message='Please fill watermark!')
            else:
                return watermark

    def add_watermark(self):
        wt = self.get_watermark()
        font = ImageFont.truetype('Symbol.ttf', 20)  # set font
        draw = ImageDraw.Draw(self.img_copy)
        draw.text((10, 10), wt, (255, 255, 255), font=font)  # add watermark
        self.img = ImageTk.PhotoImage(self.img_copy)
        self.canvas.itemconfig(
            self.image_on_canvas,
            image=self.img)  # update canvas image
        self.add_wt_success = 1

    def save(self):
        if self.add_wt_success == 1:
            img_name_list = os.path.split(self.img_copy.filename)[1].split('.')
            self.img_copy.filename = img_name_list[0] + \
                '_wt.' + img_name_list[1]  # rename photo
            file = asksaveasfile(initialfile=self.img_copy.filename)
            self.img_copy.save(file.name)  # save img to path selected by user
        else:
            messagebox.showerror(
                title='error',
                message='Pleas add watermark first!')


root = tk.Tk()
image_watermark = ImageWaterMark(root)
root.mainloop()
