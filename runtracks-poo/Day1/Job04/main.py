class Personne:
    def __init__(self, name, firstname):
        self.name = name
        self.firstname = firstname
    
    def introduce(self):
        return self.firstname +" "+ self.name

user1 = Personne("Doe", "John")
user2 = Personne("Dupond", "Jean")

print(user1.introduce())
print(user2.introduce())