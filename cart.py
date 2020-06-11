
class Cart:
    wishlist = []

    def __init__(self):
        super().__init__()
        Cart.menu()

    def add(self, product):
        self.wishlist.append(product)
        print(f"{product} added successfully")

    def remove(self, product):
        if product in self.wishlist:
            self.wishlist.remove(product)
            print(f"{product} remove successfully")
        else:
            print(f"{product} not found in the cart")

    def list(self):
        return self.wishlist

    def clear(self):
        self.wishlist = []
        return self.wishlist

    @classmethod
    def menu(cls):
        """
        """
        print(f'\nMenu:')
        print('1. Add an item?')
        print('2. Remove an item?')
        print('3. View items?')
        print('4. Exit')
        print('5. Menu')


user_cart = Cart()
flag = True

while flag:
    try:
        num = int(input('Enter your choice: '))
        if num not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid data")

        if num == 1:
            item = input('Enter the item name which you want to add: ')
            user_cart.add(item)
        elif num == 2:
            if user_cart.list():
                print("\n".join(user_cart.list()))
                item = input('Enter the item name which you want to remove: ')
                user_cart.remove(item)
            else:
                print("Your cart is empty")
        elif num == 3:
            if user_cart.list():
                print("\n".join(user_cart.list()))
            else:
                print("Your cart is empty")
        elif num == 4:
            flag = False
            if user_cart.list():
                print("You left with following items in the cart:")
                print("\n".join(user_cart.list()))
            else:
                print("Your cart is empty")
            print("\nThank you visit again")
        elif num == 5:
            user_cart.menu()
    except ValueError:
        print("Invalid Number try again\n")
        continue
