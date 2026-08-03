#q3='Which brand of coffee do you prefer?' answer=A, B

import random
import csv

brand_values = random.choices(
    ["A", "B"],
    weights=[44, 56],
    k=1500
)

with open("brand_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "brand"])
    for i, brand in enumerate(brand_values, start=1):
        writer.writerow([i, brand])

print("CSV file 'brand_data.csv' created successfully!")