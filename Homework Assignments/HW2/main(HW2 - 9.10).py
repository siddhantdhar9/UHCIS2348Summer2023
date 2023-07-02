# Siddhant Dhar - PSID: 1512852
# Zylabs 9.10: Word Frequencies (Lists)

import csv

# get filename_csv from user
filename_csv = input()

# open the filename_csv through reading the file
with open(filename_csv, 'r') as file:
    csv_reader = csv.reader(file)
    words = {}

# iterate through every word in the list to count the number of frequent words and output how many they occur in the file
    for word in csv_reader:
        for count in word:
            if count in words:
                words[count] += 1
            else:
                words[count] = 1
    for key in list(words.keys()):
        print(key, words[key])
