# Siddhant Dhar - PSID: 1512852
# Zylabs 8.10: Palindrome

word = str(input())
# Removes the spaces using the replace() method

original_word = word.replace(' ', '')

# Removes spaces starting from the last character in a word/phrase
reverse_word = word.replace(' ', '')[::-1]

# Check if the string equals itself in reverse, and if it does then it is a palindrome
if (original_word == reverse_word):
    print(word, "is a palindrome")
# Otherwise, it is not a palindrome
else:
    print(word, "is not a palindrome")