class Student:

    def __init__(self, name: str, age: int, major: str):
        self.name = name
        self.age = age
        self.major = major

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.major}")