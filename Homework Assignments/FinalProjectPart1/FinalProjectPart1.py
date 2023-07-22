# Name: Siddhant Dhar
# PSID: 1512852
# Program: Inventory Management

# Include csv and date with datetime

import csv
from datetime import date, datetime

# Read all three input files (manufacturer, price, service date) and merge into one program

# Read manufacturer list
manufacturer_dict = {}  # create an empty dictionary
with open('ManufacturerList.csv', 'r') as csvfile:
    manufacturer_list = csv.reader(csvfile, delimiter=',')

    for row in manufacturer_list:
        item_id = row[0]
        manufacturer_name = row[1]
        item_type = row[2]
        item_damaged = row[3]
        manufacturer_dict[item_id] = {
            'manufacturer_name': manufacturer_name,
            'item_type': item_type,
            'item_damaged': item_damaged}  # create dictionary with keys and values

# Read price list
price_dict = {}  # Create an empty dictionary
with open('PriceList.csv', 'r') as csvfile:
    price_list = csv.reader(csvfile, delimiter=',')

    for row in price_list:
        item_id = row[0]
        item_price = row[1]
        price_dict[item_id] = item_price  # Create dictionary with keys and values

# Read service date list
service_date_dict = {}  # Create an empty dictionary
with open('ServiceDatesList.csv', 'r') as csvfile:
    service_date_list = csv.reader(csvfile, delimiter=',')

    for row in service_date_list:
        item_id = row[0]
        service_date = row[1]
        service_date_dict[item_id] = service_date  # Create dictionary with keys and values

# Define function to sort elements in manufacturer


def sort_by_manufacturer(elem):
    return elem[1]


combined_data = []
for item_id in manufacturer_dict.keys():
    manufacturer_name = manufacturer_dict[item_id]['manufacturer_name']  # Reading the manufacturer dict and printing the values
    item_type = manufacturer_dict[item_id]['item_type']
    item_damaged = manufacturer_dict[item_id]['item_damaged']
    item_price = price_dict.get(item_id)
    service_date = service_date_dict.get(item_id)

    combined_data.append([item_id, manufacturer_name, item_type, item_price, service_date, item_damaged])

# Sort the combined data by manufacturer name in alphabetical order
combined_data.sort(key=sort_by_manufacturer)


with open('FullInventory.csv', 'w', newline='') as output_file:  # Opening the file
    writer = csv.writer(output_file) # Writing the file
    writer.writerow(['Item ID', 'Manufacturer Name', 'Item Type', 'Price', 'Service Date', 'Damaged'])
    writer.writerows(combined_data)

# Define function to sort the item IDs


def sort_by_item_id(elem):
    return elem[0]

# Sort the combined data by item ID


combined_data.sort(key=sort_by_item_id)

items_by_type = {}
for item_data in combined_data:
    item_type = item_data[2]
    if item_type not in items_by_type:
        items_by_type[item_type] = []
    items_by_type[item_type].append(item_data)

for item_type, items in items_by_type.items():
    filename = f"{item_type}Inventory.csv"
    with open(filename, 'w', newline='') as item_file: # Opening the file
        writer = csv.writer(item_file) # Writing the file
        writer.writerow(['item_id', 'manufacturer_name', 'item_type', 'price', 'service_date', 'damaged'])
        writer.writerows(items)

# Printing the current date
current_date = date.today()
print(current_date)


def sort_by_service_date(elem):
    return elem[4]


past_service_items = []
for item_id, item_data in manufacturer_dict.items():
    manufacturer_name = item_data['manufacturer_name']
    item_type = item_data['item_type']
    item_damaged = item_data['item_damaged']
    item_price = price_dict.get(item_id)
    print(service_date_dict.get(item_id))
    service_date = datetime.strptime(service_date_dict.get(item_id), '%m/%d/%Y').date()
    service_date_dict[item_id] = service_date

    if service_date < current_date:
        past_service_items.append([item_id, manufacturer_name, item_type, item_price, service_date, item_damaged])

# Sort the past service items by service date (from oldest to most recent)
past_service_items.sort(key=sort_by_service_date)  # Index 4 corresponds to the service date

# Write the past service items to PastServiceDateInventory.csv
with open('PastServiceDateInventory.csv', 'w', newline='') as past_service_file:
    writer = csv.writer(past_service_file)
    writer.writerow(['item_id', 'manufacturer_name', 'item_type', 'price', 'service_date', 'item_damaged'])
    writer.writerows(past_service_items)


def sort_by_price(elem):
    return elem[3]


damaged_items = []
for item_id, item_data in manufacturer_dict.items():
    manufacturer_name = item_data['manufacturer_name']
    item_type = item_data['item_type']
    item_damaged = item_data['item_damaged']
    item_price = price_dict.get(item_id)
    service_date = service_date_dict.get(item_id)

    if item_damaged.lower() == 'damaged':
        damaged_items.append([item_id, manufacturer_name, item_type, item_price, service_date])

# Sort the damaged items by price (from most expensive to least expensive)
damaged_items.sort(key=sort_by_price, reverse=True)  # Index 3 corresponds to the price

# Write the damaged items to DamagedInventory.csv
with open('DamagedInventory.csv', 'w', newline='') as damaged_inventory_file:
    writer = csv.writer(damaged_inventory_file)
    writer.writerow(['item_id', 'manufacturer_name', 'item_type', 'price', 'service_date'])
    writer.writerows(damaged_items)
