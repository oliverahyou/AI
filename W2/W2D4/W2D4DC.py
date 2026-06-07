#Challenge 1: Sorting
user_input = input('Enter your sentence: ')
print(user_input)
user_edit = user_input.split()
print(user_edit)

#Challenge 2: Longest Word
def find_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
find_word("Margaret's toy is a pretty doll.")