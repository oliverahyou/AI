#Exercise 1: What Are You Learning?
def display_message():
    message = "I am learning about functions in Python."
    print(message)
display_message()
# #Exercise 2: What’s Your Favorite Book?
def favorite_book(title):
    print(f"One of my favorite books is '{title}'.")
favorite_book("Can't Hurt Me by David Goggins")
#Exercise 3: Some Geography
def describe_city(city, country="Unkown"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
#Exercise 4: Random
import random
random_number= random.randint(1, 100)

def num(n):
    if 1 <= n <= 100:
        print(f" Success!")
    elif n < 1:
        print(f"{n} is less than 1")
    else:
        print(f"{n} is greater than 100")
num(random_number)
Exercise 5: Let’s Create Some Personalized Shirts!
def make_shirt(size="L", text="I love Python"):
    print(f"The shirt size is {size} and it has the text: '{text}' printed on it.")
make_shirt()
make_shirt(size="M")
make_shirt(size="S", text="Python is awesome!")
    #Exercise 6: Magicians…
# magician_names =  ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for name in magician_names:
        print(name)
def make_great(magician_names):
    for name in magician_names:
        print(f"{name} the Great")
make_great(magician_names)
show_magicians(magician_names)
#Exercise 7: Temperature Advice
def get_random_temp():
    import random
    return random.randint(-10, 40)
def main():
    temp = get_random_temp()
    print(f"The current temperature is {temp}°C.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 24:
        print("Nice weather.")

    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
main()
