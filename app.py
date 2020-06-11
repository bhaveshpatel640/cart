user_ip = 'Welcome'
data = []


def menu():
    print('Menu:')
    print('1. Add an item?')
    print('2. Remove an item?')
    print('3. View items?')
    print('4. Exit')

while user_ip != '4':

    menu()
    user_ip = input('enter your choice: ')

    if user_ip == '1':
        item = input('enter the item name: ')
        data.append(item)
        print(item, 'added to the list')

    elif user_ip =='4':
        print('Goodbye')
    
    elif user_ip == '3':
        print(data)