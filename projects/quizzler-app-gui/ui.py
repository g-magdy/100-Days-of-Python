import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.fb = None
        
        self.scoreboard = tkinter.Label(text="Score : 0")
        self.scoreboard.config(bg=THEME_COLOR, fg="white", font=("Arial", 14))
        self.scoreboard.grid(row=0, column=1)
        
        self.canvas = tkinter.Canvas(width=500, height=250)
        self.question_text = self.canvas.create_text(
            250,
            125,
            text= "",
            width=480,
            font=("Calibri", 20, "italic"),
            fill=THEME_COLOR
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_img = tkinter.PhotoImage(file="./images/true.png")
        false_img = tkinter.PhotoImage(file="./images/false.png")
        self.true_button = tkinter.Button(image=true_img, command=self.true_clicked)
        self.true_button.config(padx=20, pady=20)
        self.true_button.grid(row=2, column=0)
        
        self.false_button = tkinter.Button(image=false_img, command=self.false_clicked)
        self.false_button.config(padx=20, pady=20)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.fb:
            self.window.after_cancel(self.fb)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            msg = f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=msg)
            self.true_button.destroy()
            self.false_button.destroy()
            self.scoreboard.destroy()
        
        
    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.scoreboard.config(text=f"Score: {self.quiz.score}")
    
    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.scoreboard.config(text=f"Score: {self.quiz.score}")
        
    def give_feedback(self, answer_is_correct : bool):
        if answer_is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.fb = self.window.after(func=self.get_next_question, ms=1000)
        