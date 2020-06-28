#--------------Conditional Statements ----------------
# 1. Conditional Statements/Selection Statements
#       a. if
#       b. if - else
#       c. if - elif - else

#       a. if


name=input('Enter Name :')
if name=='akash':
    print('Hello Akash')
print('How are you ? ')

#       b. if - else
if name=='akash':
    print('Hello Akash')
else:
    print('Hello Guest')
print('How are you ? ')


#       c. if - elif - else
brand = 'Enter your brand '
if brand=='US Polo':
    print('It''s a US Brand' )
elif brand=='Gucci':
    print('It''s a rich people brand')
elif brand=='Addidas':
    print('It''s a sports brand')
else:
    print('Other brands are not recommended')

# program 2
# Program to find the biggest of given 2 numbers from the keyboard

n1=int(input('Enter first number :'))
n2=int(input('Enter second number :'))
if n1>n2:
    print('Bigger number is :',n1)
else:
    print('Bigger number is :', n2)

# program 3
# Program to print number from 0-9

n=int(input('Enter input number :'))

if n==0:
    print('Zero')
elif n==1:
    print('One')
elif n==2:
    print('Two')
elif n==3:
    print('Three')
elif n==4:
    print('One')
elif n==5:
    print('Five')
elif n==6:
    print('Six')
elif n==7:
    print('Seven')
elif n==8:
    print('Eight')
elif n==9:
    print('Nine')

else:
    print('Enter number between 0-9 only')

# nested loops
for i in range(4):
    for j in range(4):
        print('i={} and j={}'.format(i,j))


n=int(input('Enter no of rows :'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
