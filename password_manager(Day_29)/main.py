from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json
# ---------------------------- PASSWORD SEARCH ------------------------------- #


def search():
    website = w_entry.get()
    if len(website) == 0:
        messagebox.showerror(title='error', message='Website cannot be empty')
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror(message='No Data File found')
        else:
            info = data.get(website)
            if info:
                messagebox.showinfo(
                    title='password',
                    message=f"Email/Username: {data[website]['eu']}\n password: {data[website]['password']}")
            else:
                messagebox.showinfo(
                    message=f'cannot find information for this website{website}')


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
            new_data = {
                website: {
                    'eu': eu,
                    'password': password
                }
            }

            try:
                with open('data.json', 'r') as f:  # 读取历史数据
                    data = json.load(f)
            except FileNotFoundError:  # 若文件不存在则将本次数据保存
                with open('data.json', 'w') as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)  # 合并历史数据和本次数据
                with open('data.json', 'w') as f:  # 保存
                    json.dump(data, f, indent=4)
            finally:
                # 清空输入框并设定默认值
                w_entry.delete(0, END)
                eu_entry.delete(0, END)
                eu_entry.insert(0, 'test@test.com')
                pass_entry.delete(0, END)


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
w_entry = Entry(width=18)
w_entry.grid(column=1, row=1)
w_entry.focus()  # 让光标默认在此输入框

eu_entry = Entry(width=35)
eu_entry.grid(column=1, row=2, columnspan=2)  # columnspan列长度
eu_entry.insert(0, 'test@test.com')  # 默认值设定，0指输入框最左边

pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3)

# Buttons
gp_button = Button(text='Generate Password', command=password_generator)
gp_button.grid(column=2, row=3)

add_button = Button(text='Add', width=34, command=write_file)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=14, command=search)
search_button.grid(column=2, row=1)


window.mainloop()
