import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# student_score = {
#     "Alex": 89,
#     "Beth": 100,
#     "Caroline": 54,
#     "Dave": 92,
#     "Elanor": 55,
#     "Freddie": 43,
# }
# 
# Dictionary comprehension
# note = random.randint(1,100)
students_score = {student:random.randint(1,100) for student in names}
print(students_score)

#  Students that pass the test

pass_student = {student:score for student,score in students_score.items() if score >= 60}
print(pass_student)
