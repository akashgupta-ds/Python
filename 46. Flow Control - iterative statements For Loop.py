#-----------------Iterative Statements
# 2. Iterative Statements
#       a. for loop
#       b. while loop

# for loop : if we know number of iteration in advance then use for loop
# increment and decrement operator is not available in python

# Syntax
# for eachelement in sequence :
#      do some action

l=[20,30,40,60]
for i in l:
    print(i)

s='Akash Gupta'
count=0
for x in s:
    count+=1
    print(x)

s=input('Enter string :')
i=0
for x in s:
    print('The character present at ',i, 'index is ',x)
    i+=1

# increment and decrement operator is not available in python

# diplay only odd numbers between 0,20
for x in range(1,20,2):
    print('odd number for x is :',x)

# the sum of list numbers
list=eval(input('Enter some list :'))
sum=0
for x in list:
    sum=sum+x
print('The sum of numbers in list is :',sum)