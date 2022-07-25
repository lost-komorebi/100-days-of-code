from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []
for i in question_data:
    question = Question(i['text'], i['answer'])
    question_list.append(question)

quiz_b = QuizBrain(question_list, 0)
while quiz_b.still_has_next():
    quiz_b.next_question()
print('You have completed the quiz!')
print(f'Your final score is {quiz_b.score}/{len(quiz_b.question_list)}')
