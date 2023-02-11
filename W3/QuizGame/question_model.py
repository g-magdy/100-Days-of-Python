class Question:
    '''It has a text and an answer
    both should be initialized upon the creation of the question
    '''
    def __init__(self, question_text, question_answer) -> None:
        self.text = question_text
        self.answer = question_answer