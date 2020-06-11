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

   #display()
  
  # if ip == '1':
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

   # elif ip == '2':
   #    print('okay, bye!')



