#Step 1 and 2
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = farm_animals
farm_animals = {}

#Step 3
def add_animal(animal_type, count = 1):
    if animal_type not in farm_animals:
        farm_animals[animal_type] = 0
        farm_animals[animal_type] += count
    print(farm_animals) 
add_animal('goat', 5)
add_animal('cow')
add_animal('chicken', 4)

#Step 4
def get_info():
    print("McDonald's Farm")
    print('')
    for key, value in farm_animals.items():
        print(f"{key}: {value}")
    print('E-I-E-I-0!')
get_info()