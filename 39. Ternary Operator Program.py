#----------------- Ternary operator ------------------
# Syntax
# x= first value if condition 1 else second value
#       if condition 2 else third value

a= int(input('Enter first Number :'))
b= int(input('Enter second Number :'))

min = a if a < b else b
print('Minimum Value :', min)

x=10 if 20<30 else 40 if 50 <60 else 70
print(x)

c=int(input("Enter third number :"))
max= a if a>b and a> c else b if b>c else c
print('Max value is :', max)