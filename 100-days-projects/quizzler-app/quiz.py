# Importing modules
from question_model_1 import Question
from data_1 import question_data
from quiz_brain_1 import QuizBrain
from ui import QuizInterface

# Creating a question bank full of different questions
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# Initialising Quizinterface with a Quizbrain as a parameter
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
