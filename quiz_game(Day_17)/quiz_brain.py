

class QuizBrain:

    def __init__(self, question_list, question_num=0, score=0):
        self.question_list = question_list
        self.question_num = question_num
        self.score = score

    def still_has_next(self):
        return self.question_num < len(self.question_list)



    def next_question(self):
        next_q = self.question_list[self.question_num]
        self.question_num += 1
        answer = input(
            f'Q.{self.question_num} {next_q.text} (True/False):')
        self.check_answer(answer)
        print(self.question_num)

    def check_answer(self, answer):
        if answer.lower(
        ) == self.question_list[self.question_num-1].answer.lower():
            self.score += 1
            print('You are correct')
        else:
            print(
                f'You are wrong, the correct answer is: {self.question_list[self.question_num-1].answer}')
        print(f'Your score is:{self.score}')
        print('\n')
