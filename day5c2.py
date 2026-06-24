students = [
    {"name": "Jubayer", "cgpa": 3.36},
    {"name": "Mim", "cgpa": 3.57}
]

detail = {}
with open("student_detail.txt", "w") as file:
    for student in students:
        file.write(f"Name: {student['name']}, CGPA: {student['cgpa']}\n")

with open("student_detail.txt", "r") as file:
    detail = file.read()

print(detail)