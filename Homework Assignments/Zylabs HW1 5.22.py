# Zylabs 5.22: Program: Automobile service invoice

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

select_service1 = input("Select first service:\n")
select_service2 = input("Select second service:\n\n")
print("Davy's auto shop invoice\n")

cost_service1 = 0

if select_service1 == "Oil change":
    cost_service1 = 35
    print("Service 1: Oil change, $35")

elif select_service1 == "Tire rotation":
    cost_service1 = 19
    print("Service 1: Tire rotation, $19")

elif select_service1 == "Car wash":
    cost_service1 = 7
    print("Service 1: Car wash, $7")

elif select_service1 == "Car wax":
    cost_service1 = 12
    print("Service 1: Car wax, $12")

elif select_service1 == "-":
    print("Service 1: No service")


cost_service2 = 0

if select_service2 == "Oil change":
    cost_service2 = 35
    print("Service 2: Oil change, $35")

elif select_service2 == "Tire rotation":
    cost_service2 = 19
    print("Service 2: Tire rotation, $19")

elif select_service2 == "Car wash":
    cost_service2 = 7
    print("Service 2: Car wash, $7")

elif select_service2 == "Car wax":
    cost_service2 = 12
    print("Service 2: Car wax, $12")

elif select_service2 == "-":
    print("Service 2: No service")

# Calculation of total cost of the services chosen
total_cost = cost_service1 + cost_service2
print("")
print("Total: $" + str(total_cost))





