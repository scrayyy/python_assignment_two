import random

get_student_names = open("students.txt", "r", encoding="UTF-8")
student = get_student_names.read()
students = student.splitlines()
get_student_names.close()

get_exercise_titles = open("exercises.txt", "r", encoding="UTF-8")
exercise = get_exercise_titles.read()
exercises = exercise.splitlines()
get_exercise_titles.close()

for student_name in students:
    number = 1
    with open(f"{student_name}.txt", "w", encoding="UTF-8") as student:
        random_number = random.sample(exercises, 4)
        student.write(f"{number}. {random_number[0]}\n")
        number += 1
        student.write(f"{number}. {random_number[1]}\n")
        number += 1
        student.write(f"{number}. {random_number[2]}\n")
        number += 1
        student.write(f"{number}. {random_number[3]}\n")
        number = 1
print("Successful")
