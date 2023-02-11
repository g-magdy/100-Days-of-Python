from os import system
class QuizBrain:
    def __init__(self, data) -> None:
        self.questions_list = data
        self.question_number = 1
        self.score = 0
    
    def ask_question(self, q):
        '''Prints the question text to the console, recieves the input of the user and returns it as string'''
        print(f"Q{self.question_number} {q.text}")
        a = input("True or False ? ")
        # system("cls")
        return a
    
    def check_answer(self, q, user_a):
        '''prints correct/ wrong if the given answer is valid "true" or "false" returns "recheck" if it is not valid'''
        if q.answer.lower() == user_a.lower():
            self.score += 1
            print("Correct answer 👏\n")
        else:
            print("Wrong answer 😔\n")
        if self.question_number == len(self.questions_list):
            print("The quiz is finished")
            print(f"Your final score is {self.score}/{self.question_number}")
        else:
            print(f"You got {self.score} right out of {self.question_number}\n")
    
    def run(self):
        for q in self.questions_list:
            ans = self.ask_question(q)
            while ans != "true" and ans != "false":
                print("There is a typo, ")
                ans = self.ask_question(q)
            self.check_answer(q, ans)
            self.question_number += 1
