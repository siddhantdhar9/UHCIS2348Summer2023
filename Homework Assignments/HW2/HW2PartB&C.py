# Siddhant Dhar - PSID: 1512852
# Python Program that reads dates from input and checks to see whether the date is entered in the correct format.
# If the date is incorrect, then Python will end the code.


# helpful for getting the current date and time
import datetime
now = datetime.datetime.now()
print(now)

# Step 1: Define a function that gets the date, sets the original to zero, and the new date to an empty string
# Step 2: Use find(): If the date's location is not equal to -1, it will check and see which index the date is found, so that it can return a valid date
# Step 3: Use strip() to return a copy of the string with leading and trailing whitespace removed
# Step 4: Use If condition: check if date is valid and contains a "/", if not then it will set back to original date
# Step 5: Use while loop: as long as user does not enter -1, the program will loop until the user enters -1
# Step 6: Call the function to pass the valid date
def get_date_as_int(date):
     original_date = 0
     valid_date = ''
     if date.find(",") != -1:
        month_day, year = date.split(',')

        if month_day.find(" ") != 1:
            month, day = month_day.split(' ')

        original_date = 1

        day = day.strip()
        month = month.strip()
        year = year.strip()

        if month == "January":
            valid_date = '1' + '/'
        elif month == "February":
            valid_date = '2' + '/'
        elif month == "March":
            valid_date = '3' + '/'
        elif month == "April":
            valid_date = '4' + '/'
        elif month == "May":
            valid_date = "5" + "/"
        elif month == "June":
            valid_date = "6" + "/"
        elif month == "July":
            valid_date = "7" + "/"
        elif month == "August":
            valid_date = "8" + "/"
        elif month == "September":
            valid_date = "9" + "/"
        elif month == "October":
            valid_date = "10" + "/"
        elif month == "November":
            valid_date = "11" + "/"
        elif month == "December":
            valid_date = "12" + "/"
        else:
            original_date = 0

        valid_date += day + '/'
        valid_date += year

     if original_date != 1:
        return ""
     else:
        return valid_date

# part a
# parts b & c
input_file = ('C:\Users\siddh\PycharmProjects\UHCIS2348Summer2023\HW2', 'r')
input_date = input("Enter date: ")
while input_date != "-1":
    valid_date = get_date_as_int(input_date)
    if valid_date != "":
        print(valid_date)
        print('valid')
    else:
        print('not valid')
    print('')

    input_date = input()

input_file.close()
