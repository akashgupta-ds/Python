# ----------  Bitwise operators ----------
# & - if both bits are 1 then only 1 otherwise 0
# | - if atleast one bit is 1 then 1 otherwise 0
# ^ - x-or => if both args are different then 1 else 0
# ~ => bitwise complement 1==>0 and 0 ==>1
# << bitwise left shift
# >> bitwise right shift
# applicable only for int and boolean

#-----------------Identity opertors
# print( list1 is list2)   # is Compare address always
# print( list1 == list2)   # == Compare content always
#-----------------in opertors
# in operators

print(4 & 5)
print(True & True)
#print(10.5 & 10.5)  #TypeError: unsupported operand type(s) for &: 'float' and 'float'
print(True & True)
print(4 | 5)
print(4 ^ 5)
print(~ 5)
print(~ True)

# ----------  Shift operators ----------
# << => Left shift operators
# >> => Right shift operators

print(10 << 2)

# Binary to decimal
print(bin(101))

# Right shift operators
print(10>>2)

# Left shift operators
print(10<<2)

#----------------- Assignment operator------------------
x=10
print(x)
a,b,c,d=10,20,30,40
x+=10   #[Compound assignment operator]
print(x)

# x++ & x-- not works in python
# --x & ++ x but don't increament
print(-(-x))
print(+(+x))

#----------------- Compound operator------------------
# +=
# -=
# *=
# /=
# %=
# //=
# **=
# &=
# |=
# ^=
# >>=
# <<=

#----------------- Ternary operator ------------------
# Syntax
# x= first value if condition 1 else second value
#       if condition 2 else third value
x=30 if 10<20 else 40
print(x)

# Swapping
a,b=100,200
a,b=b,a

print(a)
print(b)

#----------------- Special operator ------------------
# 1. Identity operators
a,b=10,10
print(a is b)
print(a is not b)
list1=[10,20,30]
list2=[10,20,30]
print(id(list1))
print(id(list2))
print( list1 is list2)   # is Compare address always
print( list1 == list2)   # == Compare content always

# -------------In OPerator
# Result will always be in True & False

s="Hello Learning"
print('H' in s)     # True
print('i' in s)     # True
print('p' in s)     # False

# -------------Multiple OPerators operations
# operator precedence
# ()        => Parenthesis
# **        => exponential
# ~        =>  bitwise,unary
# *
# *,/,%,//
# +,-
# <<,>>
# &
# ^
# |
# >,>=,<,<=,==,!=
# =,+=,-=,*=,...
# is , is not
# in , not in
# not
# and
# or

