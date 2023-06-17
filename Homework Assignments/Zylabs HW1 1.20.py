# Zylabs 1.20: Basic output with variables

# Get a second user input into user_num1.
user_num1 = int(input("Enter integer:\n"))

# Output the user's input.
print("You entered:",user_num1)

# Calculation of input squared.
user_num2 = user_num1 * user_num1

# Output the input squared.
print(user_num1, "squared is", user_num2)

# Calculation of input cubed.
user_num3 = user_num2 * user_num1

# Output the input cubed.
print("And", user_num1, "cubed is", user_num3, "!!")

# Get a second user input into user_num2, and output the sum and product.
user_num4 = int(input("Enter another integer:\n"))

# Calculation of sum.
user_num5 = user_num1 + user_num4

# Output the sum.
print(user_num1, "+", user_num4, "is", user_num5)

# Calculation of product.
user_num6 = user_num1 * user_num4

# Output the product.
print(user_num1, "*", user_num4, "is", user_num6)