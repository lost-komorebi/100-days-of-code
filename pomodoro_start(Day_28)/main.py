"""前三个循环每工作25分钟休息5分钟，直到第四个工作25分钟结束后可以休息20分钟"""
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_f():
    """重置"""
    tick_label.config(text='')
    timer_label.config(text='Timer')
    canvas.itemconfig(canvas_text, text='00:00')
    window.after_cancel(timer)  # 停止after
    global n
    n = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

n = 0


def start_timer():
    work_min_period = int(WORK_MIN * 60)
    short_rest_period = int(SHORT_BREAK_MIN * 60)
    long_rest_period = int(LONG_BREAK_MIN * 60)

    global n
    n += 1

    if n in [1, 3, 5, 7]:
        count_down(work_min_period)
        timer_label.config(text='Work', fg=GREEN)
    elif n in [2, 4, 5]:
        count_down(short_rest_period)
        timer_label.config(text='Break', fg=PINK)
    elif n == 8:
        count_down(long_rest_period)
        timer_label.config(text='Break', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def time_formater(n):
    return '{:02}:{:02}'.format(n // 60, n % 60)


def count_down(count):
    """
    :param count: 秒
    """
    canvas.itemconfig(canvas_text, text=time_formater(count))
    if count > 0:
        global timer
        # 每隔1000毫秒就运行count_down,count-1为count_down的参数
        timer = window.after(1000, count_down, count - 1)
    else:  # 当倒计时归零后，再次触发倒计时
        start_timer()
        tick_text = n // 2 * '✔'
        tick_label.config(text=tick_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Promodoro')
window.config(padx=40, pady=40, bg=YELLOW)

timer_label = Label(
    text='Timer',
    bg=YELLOW,
    fg=GREEN,
    font=(
        FONT_NAME,
        40,
         'bold'))
timer_label.grid(column=1, row=0)

# highlightthickness=0使不同部件之间顺滑过度
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 111, image=tomato_img)
canvas_text = canvas.create_text(
    100,
    130,
    text='00:00',
    fill='white',
    font=(
        FONT_NAME,
        35,
         'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_f)
reset_button.grid(column=2, row=2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)


window.mainloop()
