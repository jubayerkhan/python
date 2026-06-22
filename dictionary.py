student = {
    "name": "Jubayer",
    "age": 25,
    "cgpa": 3.36
}

student["university"] = "UCalgary"
student["age"] = 26
print(student)

for key in student:
    print(f"{key}: {student[key]}")