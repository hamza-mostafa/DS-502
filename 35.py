class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__kind = self.__class__.__name__ or 'unknown animal'

    def eat(self):
        print(f"The {self.__kind} {self.name} is eating.")

    def sleep(self):
        print(f"The {self.__kind} {self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking: Woof! Woof!")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f"{self.name} is meowing: Meow!")

class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def fly(self):
        print(f"{self.name} is flying high in the sky!")