#Step1
class Pets:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age
class Cat(Pets):
    pass
class Siamese(Cat):
    pass
#Step2
class Bengal(Cat):
    pass
class Chartreux(Cat):
    pass
cat1 = Bengal('Cat', 'Panther', 2)
cat2 = Chartreux('Cat', 'Meow', 1)
cat3 = Siamese('Cat', 'Reow', 4)
all_cats = [cat1, cat2, cat3]

def walk():
    for cat in all_cats:
        print(f'{cat.name} is walking...')
walk()

