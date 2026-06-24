class User:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"CGPA: {self.cgpa}")

user1 = User("JK", 26, 3.36)
user2 = User("Mim", 25, 3.57)

user1.display_info()
user2.display_info()