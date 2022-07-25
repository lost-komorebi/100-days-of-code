import random
from tkinter import *
import pandas as pd
import os
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
timer = None
window = Tk()
window.title('Flashy')
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

origin_file = 'data/french_words.csv'
to_learn_file = 'data/words_to_learn.csv'


if os.path.exists(to_learn_file) and os.path.getsize(
        to_learn_file) > 1:  # 文件存在且不止包含标题
    data = pd.read_csv(to_learn_file)
else:
    data = pd.read_csv(origin_file)
# ‘records’ : list like [{column -> value}, … , {column -> value}]
data = data.to_dict(orient='records')
word = {}  # 定义变量用来保存需要学习的单词


def next_word():
    global timer
    global word
    try:
        word = random.choice(data)
    except IndexError:
        is_ok = messagebox.askokcancel(
            message="Congratulations, You have known all the words\n click ok we will close this program")
        if is_ok:
            window.destroy()
    else:
        window.after_cancel(timer)  # 取消计时器，避免在后台一直倒计时
        canvas.itemconfig(title_text, text='French', fill='black')
        canvas.itemconfig(word_text, text=word['French'], fill='black')
        canvas.itemconfig(canvas_pic, image=old_img)
        timer = window.after(3000, get_answer)  # 重新定义计时器，当点击了X或✔后会重新开始倒数


def get_answer():
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=word['English'], fill='white')
    canvas.itemconfig(canvas_pic, image=new_img)


def known():
    data.remove(word)
    df = pd.DataFrame(data)
    df.to_csv('data/words_to_learn.csv', index=False)
    next_word()


def unknown():
    df = pd.DataFrame(data)
    df.to_csv('data/words_to_learn.csv', index=False)
    next_word()


canvas = Canvas(width=800, height=526)
old_img = PhotoImage(file='images/card_front.png')
new_img = PhotoImage(file='images/card_back.png')
canvas_pic = canvas.create_image(400, 263, image=old_img)
title_text = canvas.create_text(
    400, 150, font=(
        "Ariel", 40, "italic"))
word_text = canvas.create_text(
    400, 263, font=(
        "Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

tbi = PhotoImage(file='images/right.png')
true_button = Button(
    padx=50,
    image=tbi,
    highlightthickness=0,
    command=known)
true_button.grid(column=1, row=1)
fbi = PhotoImage(file='images/wrong.png')
false_button = Button(
    padx=50,
    image=fbi,
    highlightthickness=0,
    command=unknown)
false_button.grid(column=0, row=1)
timer = window.after(3000, get_answer)
next_word()  # 调用该函数初始化先显示需要学习的单词


window.mainloop()
