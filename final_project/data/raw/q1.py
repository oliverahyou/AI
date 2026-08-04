#q1='What is your gender?' answer=male, female

import random
import csv

gender_values = random.choices(
    ["male", "female"],
    weights=[49, 51],
    k=250
)
with open("gender_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "gender"])
    for i, gender in enumerate(gender_values, start=1):
        writer.writerow([i, gender])

print("CSV file 'gender_data.csv' created successfully!")
