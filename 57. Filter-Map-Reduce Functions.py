#---------- filter()------------------------------
# if we want to filter from the group
# syntax: filter(function,sequence)
# sequence=> list,tuple,dict etc

#************
# is it possible to pass the function as argument ?
# Yes e.g. filter,map,reduce


def isEven(x):
    if x%2==0:
        return True
    else:
        return False

l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)
# even
#  It's like function filters each member of sequence/ list
l1=list(filter(lambda x:x%2==0,l))
print('Even Numbers are:',l1)
# odd
#  It's like function filters each member of sequence/ list
l2=list(filter(lambda x:x%2!=0,l))
print('Odd Numbers are:',l2)

l3= list(filter(lambda x:x*x ==25,l))
print('Filter function output for l3:',l3)

# 2. Map()
# To apply the function on each of the sequence member one by one.
# map function can be apply on multiple sequence
# here in this function executes for each of the value of sequence
# syntax: map(function,sequence)
l2= list(map(lambda x:x*x,l))
print('Map function output for l:',l2)

def double(x):
    return 2*x

l2=list(map(double,l))

print('Only function output for double l:',l2)



# 3. Reduce()
# This is use to perform the function's operation one by one on sequence through iteration
# reduce function can be apply on multiple sequence
# reduce function gives final results after calculation / applying function on each element of sequence.
# here in this function executes for each of the value of sequence
# syntax: reduce(function,iterator)
# import functools for reduce
from functools import reduce

l2=[16,18,20,22,24,26,28]
l3= reduce(lambda x,y:x*y,l2)
# 16*18*[20,22,24,26,28]=16*18*20*[22,24,26,28]=16*18*20*22*[24,26,28]=16*18*20*22*24*[26,28]=16*18*20*22*24*26*28
print('Reduce function output for l3:',l3)

l3=[0, 25, 100, 225, 400, 625, 900]
l4=[0, 25, 100, 225, 400, 625, 900]

def add_2_nos(x1,x2):
    return x1+x2

# here map adds two numbers of 2 list one by one and make a new list
# O/P map(add_2_nos,l2,l3): [16, 43, 120, 247, 424, 651, 928]
print('map(add_2_nos,l2,l3):',list(map(add_2_nos,l2,l3)))

#map(add_2_nos,l2,l3) With Lambda expression: [16, 43, 120, 247, 424, 651, 928]
print('map(add_2_nos,l2,l3) With Lambda expression:',list(map(lambda x,y:x+y,l2,l3)))

#filter(lambda x:x>15,map(add_2_nos,l2,l3)) With Lambda expression: [16, 43, 120, 247, 424, 651, 928]
# Converted to list
print('filter(lambda x:x>15,map(add_2_nos,l2,l3)) With Lambda expression:',list(filter(lambda x:x>15,map(lambda x,y:x+y,l2,l3))))

#filter(lambda x:x>15,map(add_2_nos,l2,l3)) With Lambda expression: [16, 43, 120, 247, 424, 651, 928]
# Converted to list
print('reduce(lambda x,y:x*y,filter(lambda x:x>15,map(add_2_nos,l2,l3))) :',reduce(lambda x,y:x*y,list(filter(lambda x:x>15,map(lambda x,y:x+y,l2,l3)))))


l4=reduce(lambda x,y:x*y,filter(lambda x:x>15,map(add_2_nos,l2,l3)))
print('Reduce function output for l4',l4)






