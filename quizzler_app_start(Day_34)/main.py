from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# 组装问题list
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
q_ui = QuizInterface(quiz)
q_ui.get_next_question()


