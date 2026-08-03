#q2='How old are you?' answer=18-24, 25-44, 45-64, 65+

import random
import csv
age_values = random.choices(
    ["18-24", "25-44", "45-64", "65+"],
    weights=[20, 35, 30, 15],
    k=1500
)
print(age_values[:10])

with open("age_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "age"])
    for i, age in enumerate(age_values, start=1):
        writer.writerow([i, age])

print("CSV file 'age_data.csv' created successfully!")
