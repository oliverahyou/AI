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
