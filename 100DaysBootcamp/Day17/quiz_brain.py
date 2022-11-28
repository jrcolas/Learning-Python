#Quiz Brain

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO: Asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(response, current_question.answer)

    # TODO: Checking if we're at the end of the quiz
    def still_has_questions(self):
        total_questions = len(self.question_list)
        return self.question_number < total_questions

    # TODO: Checking if the answer was correct
    def check_answer(self, user_answer, answer):
        if user_answer == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, that is incorrect.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

    def quiz_completed(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}.")