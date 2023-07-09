# Siddhant Dhar - PSID: 1512852
# Zylabs 11.18: Filter and sort a list

values_list = input()

numbers = values_list.split()

list_numbers = []

for number in numbers:
    list_numbers.append(int(number))

new_numbers = []

for number in list_numbers:
    if number >= 0:
        new_numbers.append(int(number))

new_numbers.sort()

for i in new_numbers:
    print(i, end=" ")