from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    alphabet = string.ascii_letters
    numbers = string.digits
    characters = '!@#$%^&*()'
    password = random.sample(alphabet + numbers + characters, 16)
    random.shuffle(password)
    pass_entry.delete(0, END)  # 清空密码输入框，并将新密码显示在输入框
    pass_entry.insert(0, ''.join(password))
    pyperclip.copy(''.join(password))  # 将生成的密码复制到剪贴板


# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_file():
    website = w_entry.get()
    eu = eu_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(eu) == 0 or len(password) == 0:
        messagebox.showerror(title='error', message='please fill all blanks')

    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f'Do you want to save these datas?\n email/user_name: {eu}\n password: {password}')

        if is_ok:
            # 清空输入框并设定默认值
            w_entry.delete(0, END)
            eu_entry.delete(0, END)
            eu_entry.insert(0, 'test@test.com')
            pass_entry.delete(0, END)
            data = website + ' | ' + eu + ' | ' + password + '\n'

            with open('pass.txt', 'a') as f:
                f.write(data)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

eu_label = Label(text='Email/Username:')
eu_label.grid(column=0, row=2)

pass_label = Label(text='Password:')
pass_label.grid(column=0, row=3)

# Entries
w_entry = Entry(width=35)
w_entry.grid(column=1, row=1, columnspan=2)  # columnspan列长度
w_entry.focus()  # 让光标默认在此输入框

eu_entry = Entry(width=35)
eu_entry.grid(column=1, row=2, columnspan=2)
eu_entry.insert(0, 'test@test.com')  # 默认值设定，0指输入框最左边

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Buttons
gp_button = Button(text='Generate Password', command=password_generator)
gp_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=write_file)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
