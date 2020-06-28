# Method vs Function
# Method : with in the class
# Function : outside of the class
# Python is a functional and object oriented programming language
# Method

class Student:
    def info(self):
        print('Method')

s=Student()
s.info()

# Function
# Outside of the class
def info():
    print('Function')
info()

# Important functions and Methods of list
# 1. creation of list
l=[10,20,30,40,50,60,70,90,120,400]
# length of list
print(len(l))       # function
# list item count => count(x) => occurance of x
print(l.count(10))
# list item index => index(x) => index of x
print(l.index(70))
#print(l.index(3000))        ValueError: 3000 is not in list
# ValueError: 3000 is not in list if the item not in the list
target=int(input('Enter the value to search :'))
if target in l:
    print(target,'available and its first occurence is at :',l.index(target))
else:
    print('Not Available')

# list item append => append(x) => append/add of x => to add element to list
l.append(899)
print(l)

for x in range(101):
    if x%10 == 0:
        l.append(x)

print(l)


# list item insert => insert(index,x)
# if the index is greater than last index then the element will be added at last position and vice versa

l.insert(2,900)
l.insert(-10,10001)
print(l)

# append vs insert =>
# append always added at last position of list
# insert always inserted at defined index

# extend()=> extend a list 1 with the element of list 2
l1=['Chicken','Mutton','Fish']
l2=['KF','RC','FO']
print(l1)
print(l2)
l1.extend(l2)
print('Exdended List :',l1)

# remove () and pop(index)
# reverse()
# sort()
l1.sort(reverse=True)
print('Reverse Ordered List :',l1)

#cloning => list.copy()
# When we use 'copy' to copy the list , it points to new memory location/ address
l3=l1.copy()
print('Copied List :',l3 ,'With address id at :',id(l3))
# When we use '=' aliasing to copy the list , it points to same memory location/ address from which it is assigned
# aliasing '='
l4=l1
print('Assigned List : ',l4,'With address id at :',id(l4),'From address of L1 :',id(l1))

# list operators
# '+' operator => Both should be list or same type
# '*' operator => One should be list and other should be int
l5=l1+l2
print('+ operator used l5:',l5)
l6=l1*3
print('* operator used l6:',l6)

# list compare
x=['Dog','Cat','Rat']
y=['Dog','Cat','Rat']
z=['Dog','Cat','Rat']

# The number of elements must be equal
# The order should be same
# The contents should be same (including case)


print('x==y',x==y)           # content comparison  True
print('x==z',x==z)           # content comparison  True
print('x!=z',x!=z)            # content comparison  False
print('x is y',x is y)         # reference comparison
print('x[0] is y[0]',x[0] is y[0])         # reference comparison

# we can use <,>,<=,>=
print('x > y',x>y)              # String comparison in list
# Rules
# It always compare first element of the lists
# If first elements are same then comparison will be happen between second element and so on for integer and string
# element as well.

x=[50,20,30]
y=[40,90,100,120,170]

print('x>y :',x>y)              #50 > 40
print('10 in x :',10 in x)

# remove(x), pop(index), clear()
# remove(x): to delete/remove 'x' element from the list
print('x.remove(30) :',x.remove(30))    #removal of 30 from the list
print('x list :',x)    #removal of 30 from the list
# pop(index): to get the 'indexed' element from the list
print('x.pop(1) :',x)    #pop of indexed-1  from the list
print('x list :',x)      #removal of 30 from the list
# clear(): to remove all values from the list
print('x.clear() :',x.clear())          #clear the elements from the list
print('x list :',x)    #removal of 30 from the list

# What is the difference between clear() and None
# None is to assign a list with 'None' and available for GC

# Nested List :- List of list is called nested list

ns=[10,20,[30,40]]
print('Nested List Elements :',ns[0],ns[2])
print('Nested List Elements :',ns[2][0],ns[2][1])

# Nested List as Matrix
ns1=[[10,20,30],[40,50,60],[70,80,90]]
print('Nested <Matrix> Elements :')
print('Print Elements Row Wise :')
for r in ns1:
    print(r)

print('Elements in Matrix Style')
for i in range(len(ns1)):
    #print('i=',i)
    for j in range(len(ns1[i])):
        #print('j=',j)
        print(ns1[i][j],end=' ')
    print()


# List comprehensions:

# syntax
#list = [expression for x in sequence if condition]
# length of the code is too small
# Squares of first 10 numbers
# 1st way
l1=[]
for x in range(1,11):
    l1.append(x*x)
print('Without using list comprehension :',l1)

# using list comprehension
l1=[x*x for x in range(1,11)]
print('Using list comprehension :',l1)

# Selecting only even numbers
l2=[x for x in range(1,11) if x%2==0]
print('Using list comprehension :',l2)