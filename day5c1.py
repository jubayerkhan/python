detail = {}
with open("student_records.txt", "w") as file:
    name = input("Name: " )
    age = input("age:" )
    cgpa = input("cgpa: " )
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"CGPA: {cgpa}\n")

with open("student_records.txt", "r") as file:
    detail = file.read()

print(detail)