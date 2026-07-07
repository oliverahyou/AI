#q3='Which brand of coffee do you prefer?' answer=A, B
import random
random_numbers = [random.randint(1, 2) for _ in range(1500)]
print(random_numbers[:10])
brand_map = {1: "A", 2: "B"}
brand_values = [brand_map[num] for num in random_numbers]
print(brand_values[:10])