# Python Program to calculate the age of person based on current date and the birthday of the user.
print('Birthday Calculator')
print('Current Day')
# Prompt the user to enter current date by month, day and year
currentMonth = int(input('Month: '))
currentDay = int(input('Day: '))
currentYear = int(input('Year: '))

print('Birthday')
# Prompt the user to enter birthday by month, day and year
birthMonth = int(input('Month: '))
birthDay = int(input('Day: '))
birthYear = int(input('Year: '))

# Calculation of currentAge in years
currentAge = (currentYear - birthYear)

# If condition: check if current day is equal to user's actual birthday, and if so then output 'Happy Birthday!'
if currentDay == birthDay:
    print('Happy Birthday!')

print('You are ', currentAge, " years old.")















