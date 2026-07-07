#q1='What is your gender?' answer=male, female
import random
random_numbers = [random.randint(1, 2) for _ in range(1500)]
print(random_numbers[:10])
gender_map = {1: "male", 2: "female"}
gender_values = [gender_map[num] for num in random_numbers]
print(gender_values[:10])
