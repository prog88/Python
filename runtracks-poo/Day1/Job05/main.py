class Animal:
    def __init__(self, age = 0, first_name = ""):
        self.age = age
        self.first_name = first_name

    def grown(self):
        self.age += 1

    def display_age(self):
        print(f"Animal age is {self.age}")

    def rename(self, new_name):
        self.first_name = new_name

    def introduce(self):
        print(f"Animal name is {self.first_name}")

anAnimal = Animal()
anAnimal.display_age()
anAnimal.grown()
anAnimal.display_age()
anAnimal.rename("Luna")
anAnimal.introduce()