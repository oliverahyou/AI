#Exercise1
class Pets:
    def __init__(self, pets_list):
        self.pets = pets_list

    def walk(self):
        for pet in self.pets:
            print(f'{pet.name} is walking...')
class Cat:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age
class Siamese(Cat):
    pass
class Bengal(Cat):
    pass
class Chartreux(Cat):
    pass
cat1 = Bengal('Bengal', 'Panther', 2)
cat2 = Chartreux('Chartreux', 'Meow', 1)
cat3 = Siamese('Siamese', 'Reow', 4)
all_cats = [cat1, cat2, cat3]
sara_pets = Pets(all_cats)
sara_pets.walk()
