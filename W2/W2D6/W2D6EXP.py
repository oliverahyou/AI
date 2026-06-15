# Exercise 1: Cats
# Step 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("Whiskers", 1)
cat2 = Cat("Mittens", 2)
cat3 = Cat("Fluffy", 4)

# Step 2
def find_oldest_cat(cat1, cat2, cat3):
    cat = [cat1, cat2, cat3]

    oldest_cat = cat[0]
    for i in cat:
        if i.age > oldest_cat.age:
            oldest_cat = i
    return i
print(f"The oldest cat is {find_oldest_cat(cat1, cat2, cat3).name}, and it is {find_oldest_cat(cat1, cat2, cat3).age} years old.")


#Excercises 3: Dogs

