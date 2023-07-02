# Siddhant Dhar - PSID: 1512852
# Zylabs 6.17: Password modifier

word = input()
password = ''

# Create a for loop to iterate the number of occurrences in a string
for character in word:

    # If the character is in the word the user inputs,
    # then the character in the word will be replaced with the new strongest character
    if character == 'i':
        word = word.replace('i', '!')
    elif character == 'a':
        word = word.replace('a', '@')
    elif character == 'm':
        word = word.replace('m', 'M')
    elif character == 'B':
        word = word.replace('B', '8')
    elif character == 'o':
        word = word.replace('o', '.')
    # Otherwise, the user will replace an empty space, with an exclamation point
    else:
        word = word.replace(' ', '!')

    # Append the word with an exclamation point to complete the password
    password = word + 'q*s'

print(password)