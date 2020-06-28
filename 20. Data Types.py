#-----------Data type--------------------
# 1. Dynamically typed language programming.
# 2. No need to declare variable explicitly

# 14 Data Types
# int 10,20
# float 10.230
# complex => 10+20j
# bool => True , False
# str => String => 'Akash'
# bytes => A group of byte values
# bytearray => Array of bytes
# range => represent a range of numbers
# list => A group of values (mutable)
# tuple =>  A group of values (immutable)
# set => A list of values without duplicates (mutable)
# frozenset => A list of values without duplicates but we can't modify (immutable)
# dict => key-value pair
# None => Nothing is there

#import dataclasses
print(type)
# 1. int() : integral values - 10,20,30
a=10
print(type(a))   # <class 'int'>
#long => python 3. not available

# Representing int value by following 4 forms

# 1. Decimal form   ( Base 10)  => 0-9 => a = 7878
a = 7878
print(type(a))
# 2. Binary form    ( Base 2)  => 0-1  => a= 0b1111
# a= 0b1111
print(bin(a))
print(type(bin(a)))
# 3. Octal form     ( Base 8)  => 0-7  => a=0O777
# a= 0O777
print(oct(a))
print(type(oct(a)))
# 4. Hexa decimal   ( Base 16)  => 0-9 , a to f, A to F => a=0XFace
#a= 0XFace
print(hex(a))
print(type(hex(a)))
# 4. Bool data type => True  False
# in quotes word python treat it a string

print(True + True )  #=>2
print(True + False )  #=>1

# 5.  Str Data type => Any sequence of character is called string
s='Python'
# for multiline
s='''Python                 or   '''   '''Programming   '''

print(s)




