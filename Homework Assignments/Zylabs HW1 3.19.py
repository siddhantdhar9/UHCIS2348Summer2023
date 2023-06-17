# Zylabs 3.19: Program: Painting a wall

import math  # needed in Step #3

# Reference from Zybooks Chapter 3.5 (Accessing dictionary entries)
# Read from input wall height, wall width, and cost of one paint can (floats).
# Calculate and output the wall's area to one decimal place using print(f"Wall area: {wall_area:.1f} sq ft");

wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))

wall_area = wall_height * wall_width

print(f"Wall area: {wall_area} square feet")

# Calculate and output the amount of paint needed to three decimal places.
# One gallon of paint covers 350 square feet.

paint_amount = wall_area / 350

# print(f"Paint needed: {paint_amount:.2f} gallons")
print('Paint needed: {:.2f} gallons'.format(paint_amount))

# Calculate and output the number of 1 gallon cans needed to paint the wall.
# Extra paint may be left over. Hint: Use ceil() from the math module to round up to the nearest gallon (int).

can_amount = math.ceil(paint_amount)

print(f"Cans needed:", can_amount, "can(s)\n")

# Prompt the user for a color they want to paint the walls
paint_color = str(input("Choose a color to paint the wall:\n"))
# Use a dictionary to associate each paint color with its respective cost.
user_colors = {'red': 35, 'blue': 25, 'green': 23}
# Calculate the total cost of the paint cans depending on which color is chosen.
total_cost = user_colors[paint_color] * can_amount
# Output the total cost of purchasing the type of color chosen
print(f'Cost of purchasing', paint_color, "paint: $"+str(total_cost))
