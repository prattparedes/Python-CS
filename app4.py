#Modules and Pip
import useful_tools
import docx

print(useful_tools.roll_dice(10))
# docx.

# Classes and Objects
from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Mike", "Sciences", 4.1, True)
student3 = Student("Lara", "Art", 2.3, True)

# print(student1)
# print(student1.gpa)
# print(student2.name)
# print(student3.major)

# Multiple Choice Quiz
from Question import Question

questions_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score is: " + str(score) + "/" + str(len(questions)) + " Correct Answers")

# run_test(questions)

#Object Functions
from Student import Student2

student1 = Student2("Oscar", "Accounting", 3.1)
student2 = Student2("Phill", "Business", 3.7)

print(student2.on_honor_roll())
print(student1.on_honor_roll())