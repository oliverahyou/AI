#q2='How old are you?' answer=18-24, 25-44, 45-64, 65+
import random
random_numbers = [random.randint(18, 70) for _ in range(1500)]
print(random_numbers)