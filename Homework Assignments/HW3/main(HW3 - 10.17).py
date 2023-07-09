# Siddhant Dhar - PSID: 1512852
# Zylabs 10.17: Warm up: Online shopping cart (Part 1)

# Type code for classes here
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $' + str(
            self.item_quantity * self.item_price))


if __name__ == "__main__":
    # Type main section of code here
    print('Item 1')
    item_price1 = ItemToPurchase()
    item_price2 = ItemToPurchase()

    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item_price1.item_name = name
    item_price1.item_price = price
    item_price1.item_quantity = quantity

    print('\nItem 2')
    name2 = input('Enter the item name:\n')
    price2 = int(input('Enter the item price:\n'))
    quantity2 = int(input('Enter the item quantity:\n'))
    item_price2.item_name = name2
    item_price2.item_price = price2
    item_price2.item_quantity = quantity2

    print('\nTOTAL COST')
    item_price1.print_item_cost()
    item_price2.print_item_cost()
    total = (item_price1.item_price * item_price1.item_quantity) + (item_price2.item_price * item_price2.item_quantity)

    print('\nTotal: $' + str(total))




