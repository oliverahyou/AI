#q2='How old are you?' answer=18-24, 25-44, 45-64, 65+
import random
random_numbers = [random.randint(1, 4) for _ in range(1500)]
print(random_numbers[:10])
age_map = {1: "18-24", 2: "25-44", 3:"45-64", 4:"65+"}
age_values = [age_map[num] for num in random_numbers]
print(age_values[:10])
