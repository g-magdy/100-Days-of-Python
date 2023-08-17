import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

def main():
    question_data = get_data()
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


    quiz = QuizBrain(question_bank)
    QuizInterface(quiz)
    

def get_data() -> dict:
    parameters = {
        "amount":10,
        "type":"boolean",
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]


main()