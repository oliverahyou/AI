#Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat('Whiskers', 1)
cat2 = Cat('Mittens', 2)
cat3 = Cat('Fluffy', 4)

# Step 2
def find_oldest_cat(cat1, cat2, cat3):
    cat = [cat1, cat2, cat3]

    oldest_cat = cat[0]
    for i in cat:
        if i.age > oldest_cat.age:
            oldest_cat = i
    return i
print(f"The oldest cat is {find_oldest_cat(cat1, cat2, cat3).name}, and it is {find_oldest_cat(cat1, cat2, cat3).age} years old.")

#Excercises 2
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
dog1 = Dog('Jake', 50)

def bark(dog_name):
    print(f'{dog_name} goes "Woof!"')
bark(dog1.name)

def jump(dog_height):
    jump_height = dog_height * 2
    return jump_height

print(f'{dog1.name} can jump {jump(dog1.height)} cm high!')

davids_dog = Dog('Rex', 40)
sarahs_dog = Dog('James', 20)

bark(davids_dog.name)
bark(sarahs_dog.name)
print(f'{davids_dog.name} can jump {jump(davids_dog.height)} cm high!')
print(f'{sarahs_dog.name} can jump {jump(sarahs_dog.height)} cm high!')

#Exercise 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

def sing_me_a_song():
    for i in stairway.lyrics:
        print(i)
sing_me_a_song()

#Exercise 4
#Step 1

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = animals
animals = []
def add_animal(new_animal):
        animals.append(new_animal)
add_animal('Lion')
add_animal('Lion')

def get_animals():
    print(animals)
get_animals()

def sell_animal(animal_sold):
    animals.remove(animal_sold)
sell_animal('Lion')
get_animals()

def sort_animals():
    animals.sort()

#map()?
