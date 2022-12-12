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

print(student1)
print(student1.gpa)
print(student2.name)
print(student3.major)