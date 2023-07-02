# Siddhant Dhar - PSID: 1512852
# Zylabs 6.22: Brute Force Equation Solver

''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

integer_solution = False

''' Type your code here. '''
for x in range(-10, 10 ):
    for y in range(-10, 10):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x, y)
            integer_solution = True
if integer_solution != True:
    print("No solution")