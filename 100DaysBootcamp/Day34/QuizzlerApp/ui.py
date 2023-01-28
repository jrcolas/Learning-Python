from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.canvas = Canvas(width=300, height=250)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="The Text Goes Here",
                                                     font=("Arial", 18, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)

        self.score_lbl = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_lbl.grid(column=1, row=0)

        self.true_btn = Button(image=true_img, highlightthickness=0, border=0, command=self.pressed_true)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=false_img, highlightthickness=0, border=0, command=self.pressed_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.update_score()
        else:
            self.canvas.config(bg="red")
        self.window.after(1500, self.get_next_question)

    def update_score(self):
        self.score = self.quiz.score
        self.score_lbl.config(text=f"Score: {self.score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz. "
                                        f"Your final score was {self.score}/10. Press X to exit.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(command=exit)

    def pressed_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def pressed_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

