from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    text = q["text"]
    answer = q["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)


print(question_bank[0].text)