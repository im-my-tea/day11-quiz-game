class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.question_list = list

    def next(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"{self.question_number}: {current.text}(True/False): ")
        self.check(answer, current.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check(self, answer, correct):
        if answer.lower() == correct.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That is wrong!")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")