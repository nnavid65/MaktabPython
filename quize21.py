# writing class

class Animal():
    def __init__(self, name, species, age, sound, zoo_name):
        self.name = name 
        self.species = species
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name

    def make_sound(self):
        print(f"{self.name} the {self.species} says: {self.sound}")

    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.species} and the Zoo Name is {self.zoo_name}."
    
    def __str__(self):
        return f"{self.name} is a {self.age}-year-old {self.species} and the Zoo Name is {self.zoo_name}."
    

class Bird(Animal):
    def __init__(self, name, species, age, sound, zoo_name, wing_span):
        super().__init__(name, species, age, sound, zoo_name)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} the {self.species} chirps: {self.sound}")

animal_1 = Animal("Leo", 'Lion', 5, 'Roar', 'Asqar Zoo')
animal_1.make_sound()
print(animal_1.info())
print(animal_1)

bird_1 = Bird("Tweety", 'Canary', 2, 'Tweet', 'Asqar Zoo', '15cm')
bird_1.make_sound()
print(bird_1.info())
print(bird_1)

print(animal_1.name)
print(animal_1.species)
print(animal_1.age)
print(animal_1.sound)

