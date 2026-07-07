#q2='How old are you?' answer=18-24, 25-44, 45-64, 65+

import random
import csv

random_numbers = [random.randint(1, 4) for _ in range(1500)]
print(random_numbers[:10])
age_map = {1: "18-24", 2: "25-44", 3:"45-64", 4:"65+"}
age_values = [age_map[num] for num in random_numbers]
print(age_values[:10])

with open("age_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "age"])
    for i, age in enumerate(age_values, start=1):
        writer.writerow([i, age])

print("CSV file 'age_data.csv' created successfully!")
