# Siddhant Dhar - PSID: 1512852
# Zylabs 2.20: Program - Cooking measurement converter

# FIXME (1): Finish reading other items into variables, then output the three ingredients
lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))

user_servings = int(input("How many servings does this make?\n\n"))

print("Lemonade ingredients - yields", '{:.2f}'.format(user_servings), "servings")

print('{:.2f}'.format(lemon_juice_cups), "cup(s) lemon juice")
print('{:.2f}'.format(water_cups), "cup(s) water")
print('{:.2f}'.format(agave_nectar_cups), "cup(s) agave nectar\n")

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
desired_servings = int(input("How many servings would you like to make?\n\n"))

lemon_juice_cups = (lemon_juice_cups / user_servings) * desired_servings
water_cups = (water_cups / user_servings) * desired_servings
agave_nectar_cups = (agave_nectar_cups / user_servings) * desired_servings

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format(lemon_juice_cups), "cup(s) lemon juice")
print('{:.2f}'.format(water_cups), "cup(s) water")
print('{:.2f}'.format(agave_nectar_cups), "cup(s) agave nectar\n")

# FIXME (3): Convert and output the ingredients from (2) to gallons

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format(lemon_juice_cups / 16), "gallon(s) lemon juice")
print('{:.2f}'.format(water_cups / 16), "gallon(s) water")
print('{:.2f}'.format(agave_nectar_cups / 16), "gallon(s) agave nectar")







