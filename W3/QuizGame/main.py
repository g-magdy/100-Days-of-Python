from os import system
from quiz_data import old_question_data, new_quiz_data
from question_model import Question
from quiz_brain import QuizBrain

system("cls")

question_bank = []
for quest in new_quiz_data:
    txt = quest["question"]
    ans = quest["correct_answer"]
    question_bank.append(Question(txt, ans))
    
quiz_game = QuizBrain(question_bank)
quiz_game.run()