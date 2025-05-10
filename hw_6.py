# Delilah medina
# table of 2

y = int(input("Enter a number no greater than 32: "))
while y not in range(0, 33):
    y = int(input("Enter a number no greater than 32: "))


for x in range(y):
    print(x ,2 ** x)
