farm_animals = {}
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = farm_animals
    def add_animal(self, animal_type, count = 1):
        if animal_type not in farm_animals:
            farm_animals[animal_type] = 0
            farm_animals[animal_type] += count
    def get_info(self):
        print("McDonald's Farm")
        print('')
        for key, value in farm_animals.items():
            print(f"{key}: {value}")
        print('E-I-E-I-0!')

mcdonalds_farm = Farm("McDonald's Farm")    
mcdonalds_farm.add_animal('cow', 4)
mcdonalds_farm.add_animal('chicken', 15)
mcdonalds_farm.get_info()


