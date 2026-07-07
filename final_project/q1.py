#q1='What is your gender?' answer=male, female

import random
import csv

random_numbers = [random.randint(1, 2) for _ in range(1500)]
print(random_numbers[:10])
gender_map = {1: "male", 2: "female"}
gender_values = [gender_map[num] for num in random_numbers]
print(gender_values[:10])

with open("gender_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "gender"])
    for i, gender in enumerate(gender_values, start=1):
        writer.writerow([i, gender])

print("CSV file 'gender_data.csv' created successfully!")
