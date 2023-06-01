import html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_question = None
        self.score = 0

    def still_got_questions(self):
        return self.question_number != len(self.question_list)

    def check_answer(self,current_ans):
        ans = self.current_question.ans
        if ans.lower() == current_ans.lower():
            self.score += 1
            return True
            # print('You got it right!')
        else:
            return False
            # print("That's wrong.")
        # print(f'Your current score is: {self.score}/{self.question_number}')
        # print('\n')

    def next_question(self):

        """Returns question based on current ques_no"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        # ans = input(f'Q.{self.question_number}: {q_text} (True/False)?: ')
        # self.check_answer(ans, current_question.ans)
        return f'Q.{self.question_number}: {q_text}'

