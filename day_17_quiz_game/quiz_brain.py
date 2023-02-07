class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_got_questions(self):
        return self.question_number != len(self.question_list)

    def check_answer(self, ans, current_ans):
        if ans.lower() == current_ans.lower():
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong.")
        print('The correct answer was:', current_ans)
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')

    def next_question(self):
        """Returns question based on current ques_no"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        self.check_answer(ans, current_question.ans)


