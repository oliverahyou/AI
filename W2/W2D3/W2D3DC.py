import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728
seen = set()
for number_one in list_of_numbers:
    number_two = target_number - number_one

    if number_two in seen:
        print(f"{number_one} and {number_two} sums up to {target_number}")  
    seen.add(number_one)
print(seen)