from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    text = q["text"]
    answer = q["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")