#------------Relational Operators -----------------
# >,<=,<,>=

a='durga'          #'durga'
b='akash'

print("a>b is ", a>b) # True based on  A & D
print("a>=b is ", a>=b) # True based on  A & D
print("a<b is ", a<b) # False based on  A & D
print("a<=b is ", a<=b) # False based on  A & D

# Based on unicode relational operator or alphabetical order (ASCII Code)

print('ASCII =',ascii('A'))
print('ASCII =',ascii('a'))

# for boolean we use relational operator
# for different types the type error will throw

a=True
b=False


print("a>b is ", a>b) # True based on  A & D
print("a>=b is ", a>=b) # True based on  A & D
print("a<b is ", a<b) # False based on  A & D
print("a<=b is ", a<=b) # False based on  A & D

# for different types the type error will throw

a=10
b=20
if(a>b):
    print('a is greater than b ')
else:
    print('b is greater than a ')

# chaining of relational operator is possible
a,b,c,d=10,20,30,40
if (a<b<c<d):
    print('One of the operator false then false')


