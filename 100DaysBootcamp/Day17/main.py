from question_model import Question
from data import question_data, other_data
from quiz_brain import QuizBrain

question_bank = []


for each_question in other_data:
    question_text = each_question["question"]
    question_answer = each_question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.quiz_completed()
