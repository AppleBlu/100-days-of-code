class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_guess = ''
        self.user_score = 0

    def next_question(self):
        self.question_number += 1
        self.user_guess = input(
            f'Q.{self.question_number}: {self.question_list[self.question_number - 1].text} (True or '
            f'False)?: ')

    def still_has_questions(self):
        if self.question_number < 12:
            return True
        else:
            return False

    def check_answer(self):
        if self.user_guess == self.question_list[self.question_number - 1].answer:
            print(f'Correct!!! It was {self.question_list[self.question_number - 1].answer}')
            self.user_score += 1
            score = f'[{self.user_score}/{self.question_number}]'
            print(f'Your current score is: {score}\n')
        else:
            print(f'Incorrect. It was {self.question_list[self.question_number - 1].answer}')
            score = f'[{self.user_score}/{self.question_number}]'
            print(f'Your current score is: {score}\n')
