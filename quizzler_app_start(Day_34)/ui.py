from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score:0', pady=20, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.quiz_text = self.canvas.create_text(
            150, 125, text="", width=250, font=(
                "Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_img,
            highlightthickness=0,
            command=self.get_true)
        self.true_button.grid(row=2, column=0, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_img,
            highlightthickness=0,
            command=self.get_false)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text, fill='black')
        else:
            self.canvas.itemconfig(self.quiz_text,
                                   text='You have reached the end of this quiz')
            self.true_button.config(state='disabled')  # 使按钮无法再点击
            self.false_button.config(state='disabled')

    def get_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def get_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.score_label.config(text=f'Score:{self.quiz.score}')
        self.window.after(1000, self.get_next_question)
