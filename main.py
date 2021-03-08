# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.user = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Sandeep")
# user_2 = User("002", "Ankit")
#
# print(user_1.id + "\n" + user_1.user)
# print(user_1.followers)
# user_1.follow(user_2)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

from quiz_data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()

print("You've competed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
