user_ip = 'Welcome'
ip = 'hi'
data = []

def display():
    print('Main menu: ')
    print('1. View menu?' )
    print('2. Exit? ')
display()
ip = input('Enter your choice: ')

while ip == '1':

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
         print('The items in your list are:', *data, sep='\n')

      elif user_ip =='2':
          user_ip = input('Enter the name of item you wish to remove: ')
          if user_ip in data:
              data.remove(user_ip)
              print(user_ip, 'removed sucessfully.')
          else:
              print(user_ip, 'is not added in the list yet.')
      elif user_ip != '1' or '2' or '3' or '4' :
          print('invalid input, please try again.')

if ip == '2':
    print('okay, bye!')
