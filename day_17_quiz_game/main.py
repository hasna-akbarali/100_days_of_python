from question_model import QuestionModel
from data import question_data
from computer import computer_questions
from quiz_brain import QuizBrain

# data.py is the dataset
# for question in question_data:
#     question_text = question["text"]
#     question_ans = question["answer"]
#     question_bank.append(QuestionModel(question_text, question_ans))

set_of_questions = computer_questions["results"]
"""Created a question bank based on our data"""
question_bank = []

for question in set_of_questions:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    question_bank.append(QuestionModel(question_text, question_ans))

my_quiz_brain = QuizBrain(question_list=question_bank)

while my_quiz_brain.still_got_questions():
    my_quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {my_quiz_brain.score}/{my_quiz_brain.question_number} ")