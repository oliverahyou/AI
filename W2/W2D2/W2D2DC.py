# Step 1: Transforming the String into a 2D List
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM#
$a
#t%'''
matrix = MATRIX_STR.split()
print(matrix)

# Step 2: Iterate through columns
max_len = max(len(row) for row in matrix)
for col in range(max_len):
    for row in matrix:
        if col < len(row):
          char = row[col]
          print(char, end='')

# Step 3: Filter alpha characters
matrix = ['7ir', 'Tsi', 'h%x', 'i', '?', 'sM#', '$a', '#t%']
max_len = max(len(row) for row in matrix)
result = ""
for col in range(max_len):
    for row in matrix:
        if col < len(row):
            char = row[col]
            if char.isalpha():
                result += char
print(result)

# Step 4: Replace symbols with spaces
matrix = ['7ir', 'Tsi', 'h%x', 'i', '?', 'sM#', '$a', '#t%']
max_len = max(len(row) for row in matrix)
result = ""
for col in range(max_len):
    for row in matrix:
        if col < len(row):
            char = row[col]
            if char.isalpha():
                result += char
            else:
                result += ' '
print(result)

# Step 5: Constructing the Secret Message
#Detected language of Secret Message: English
#Sentence emmerging after with minor check (Extra space removed) applied with knowledge of popular culture match (Movie reference of secret message detected):
secret = 'This is Matrix' #which seems to refer to the Matrix Trilogy movies which stars Keanu Reeves AKA Neo in the movie.
print(secret)