from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.card_text = Label(text='Score : 0', font=('Arial', 18, 'italic'), bg=THEME_COLOR, fg='white')
        self.card_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.rectangle = self.canvas.create_rectangle(0, 0, 300, 250, fill='white', outline='')
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text='', font=('Arial', 20, 'italic'), fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.check = PhotoImage(file='images/true.png')
        self.check_btn = Button(image=self.check, highlightthickness=0, command=self.check_btn_cmd)
        self.check_btn.grid(row=2, column=0)

        self.cross = PhotoImage(file='images/false.png')
        self.cross_btn = Button(image=self.cross, highlightthickness=0, command=self.cross_btn_cmd)
        self.cross_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.rectangle, fill="white")
        if self.quiz.still_got_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz')
            self.cross_btn.config(state='disabled')
            self.check_btn.config(state='disabled')

    def check_btn_cmd(self):
        ans = self.quiz.check_answer("true")
        self.color_change(ans)

    def cross_btn_cmd(self):
        ans = self.quiz.check_answer("false")
        self.color_change(ans)

    def color_change(self, ans):
        if bool(ans):
            self.canvas.itemconfig(self.rectangle, fill="#7EED83")

        else:
            self.canvas.itemconfig(self.rectangle, fill="#ED897E")

        self.window.after(1000, self.get_next_question)
        self.card_text.config(text=f'Score : {self.quiz.score}')
