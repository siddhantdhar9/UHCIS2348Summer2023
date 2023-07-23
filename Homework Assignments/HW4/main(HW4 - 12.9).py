# Siddhant Dhar - PSID: 1512852
# Zylabs 12.9: Exception handling to detect input string vs. integer


# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:    # Insert try/except blocks to catch the exception
        age = int(parts[1]) + 1
    except ValueError as excpt:
        age = 0     # Output 0 for the age

    # Get next line
    # Print f string with name followed by age
    print(f'{name} {age}')
    parts = input().split()
    name = parts[0]