# Delilah Medina 
# Rewrite your program using try and expect so that your program handles
# non-numeric input gracefully by printing message and exiting the
# program.
 
try:
    hour = int(input("Enter hours: "))
    rate = input('Enter rate: ')
    pay= hour * float(rate)

    print(f'pay: {pay:.2f}')
except:
   print('please enter a number.')

