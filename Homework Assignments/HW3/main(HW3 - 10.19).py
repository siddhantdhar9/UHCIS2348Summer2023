# Siddhant Dhar - PSID: 1512852
# Zylabs 10.19: Online shopping cart (Part 2)

# Type code here
class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(int(self.item_price)) + ' = $' + str(
            int(self.item_price * self.item_quantity)))

    def print_item_description(self):  # add print description method on for part 2
        print(self.item_name + ': ' + self.item_description)


# Initialize class ShoppingCart
class ShoppingCart:
    def __init__(self, customer_name='', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):  # add items info into list
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, itemName):  # remove items from the list only if it already in the cart
        removeItem = False
        for i in self.cart_items:
            if i.item_name == itemName:
                self.cart_items.remove(i)
                removeItem = True
                break
        if not removeItem:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase):  # retrieving info of item from ItemToPurchase class and modify item
        modifyItem = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == ItemToPurchase.item_name:
                modifyItem = True
                if (
                        ItemToPurchase.item_price == 0 and ItemToPurchase.item_quantity == 0 and ItemToPurchase.item_description == 'none'):  # checking default
                    break
                else:
                    if (ItemToPurchase.item_price != 0):
                        self.cart_items[i].item_price = ItemToPurchase.item_price
                    elif (ItemToPurchase.item_quantity != 0):
                        self.cart_items[i].item_quantity = ItemToPurchase.item_quantity
                    elif (ItemToPurchase.item_description != 'none'):
                        self.cart_items[i].item_description = ItemToPurchase.item_description
                    break
        if not modifyItem:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        numItems = 0  # quantity initilized as 0 (empty) and increase and item added
        for i in self.cart_items:
            numItems += i.item_quantity
        return numItems

    def get_cost_of_cart(self):
        totalCost = 0  # calculate cost by  item quantity multiply to cost of that item
        Cost = 0
        for i in self.cart_items:
            Cost = i.item_quantity * i.item_price
            totalCost += Cost
        return totalCost

    def print_total(self):
        totalCost = self.get_cost_of_cart()  # print total cost if only cart is not empty
        if totalCost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print('Number of Items: ' + str(self.get_num_items_in_cart()) + '\n')
            for i in self.cart_items:
                i.print_item_cost()

            print('\nTotal: $' + str(totalCost))

    def print_description(self):
        if len(self.cart_items) == 0:  # print description if only item already define in cart
            print('SHOPPING CART IS EMPTY')
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()

    def print_menu(newCart):
        customerCart = newCart
        menu = ('\nMENU\n'
                'a - Add item to cart\n'
                'r - Remove item from cart\n'
                'c - Change item quantity\n'  # creating menu for selection desire, each letter corresponding to methods defined above
                "i - Output items' descriptions\n"
                'o - Output shopping cart\n'
                'q - Quit\n')
        cmd = ''
        while cmd != 'q':
            print(menu)
            cmd = input('Choose an option:\n')
            while (cmd != 'a' and cmd != 'o' and cmd != 'i' and cmd != 'q' and cmd != 'r' and cmd != 'c'):
                cmd = input('Choose an option:\n')
            if cmd == 'a':
                print("ADD ITEM TO CART")
                item_name = input('Enter the item name:\n')
                item_description = input('Enter the item description:\n')
                item_price = int(input('Enter the item price:\n'))
                item_quantity = int(input('Enter the item quantity:\n'))
                itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                customerCart.add_item(itemtoPurchase)
            elif cmd == 'o':
                print('OUTPUT SHOPPING CART')
                customerCart.print_total()
            elif cmd == 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                customerCart.print_description()

            elif cmd == 'r':
                print('REMOVE ITEM FROM CART')
                itemName = input('Enter name of item to remove:\n')
                customerCart.remove_item(itemName)
            elif cmd == 'c':
                print('CHANGE ITEM QUANTITY')
                itemName = input('Enter the item name:\n')
                Qty = int(input('Enter the new quantity:\n'))
                itemToPurchase = ItemToPurchase(itemName, 0, Qty)
                customerCart.modify_item(itemToPurchase)


if __name__ == "__main__":
    # Type main section of code here
    customerName = input("Enter customer's name:\n")
    Date = input("Enter today's date:\n")

    print("\nCustomer name: {}\nToday's date: {}".format(customerName, Date))

    newCart = ShoppingCart(customerName, Date)
    newCart.print_menu()