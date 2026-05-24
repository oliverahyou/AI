#Challenge 1: Multiples of a Number
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
num_counter = []
while len(num_counter) < length:
    number_inc = number * (len(num_counter) + 1)
    num_counter.append(number_inc)
    print(len(num_counter))
print(num_counter)
#Challenge 2: Remove Consecutive Duplicate Letters
# The below is an initial approach to the challenge. Further refinement is needed to ensure all consecutive duplicates are removed for more complex cases. 'It works for "Hii"', but not for 'potatoo'.
user_input = input("Enter a word: ")
letters = list(user_input)
print()
for i in letters:
   if letters.count(i) > 1:
       letters.remove(i)
       new_str = ''.join(letters)
   elif letters.count(i) == 1:
       new_str = ''.join(letters)
print(f'The string is currently: {new_str}')
a_str = input("Enter a string: ")
e = list(a_str)
b_str = ""
for i, x in enumerate(e):   
   nextelem = e[(i + 1) % len(e)]  
   if nextelem == x:
      print("Duplicate found, removing")
   else:
       b_str = b_str + x
print(b_str)
