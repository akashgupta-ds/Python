# --------------- Python 2.0-------------------
# We required to use typecasting functions
#x= raw_input("Enter the number1 :")

# python 2.0
# We don't required to provide typecasting function
x= input("Enter the number1 :")

# python 3.0
# This input is same as raw_input of python 3.0,We are required to provide typecasting function to convert
# raw_input() of Python 2.0 is equivalent to input() of Python 3.0
y= input("Enter the number2 :")
z= input("Enter the number3 :")
# input requires typecasting to int

print('The sum of numbers is :',(x+y+z))

# Imp **************************************
# How to read multiple values from the keyword in a single line
a,b=[int(x) for x in input('Enter 2 numbers:').split()]
print(a+b)

a,b=[float(x) for x in input('Enter 2 float numbers:').split(',')]
print(a+b)

# eval ()
# always takes input as string and result will be evaluated correspondigly
# whatever the data we provide it eval converts internally to that data type