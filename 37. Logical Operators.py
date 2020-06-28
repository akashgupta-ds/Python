# ----------- Logical Operator ----------------
# and => if both arg are true then true
# or => if one arg is true then true
# Not => if true then false

# for non-boolean types

print(True and False)
print(True and True)
print(not True)
print(True or False)

#for non-boolean types :-
# Rule
# 0 means false
# non-zero means True
# empty string => false

# if x evaluates to false then result is x otherwise returns y
# x and y
print(10 and 20)        #20
print(0 and 20)         #0
print(1 and 'abc')      #abc
print(0 and 'abc')      #0

# if x evaluates to true then result is x otherwise returns y
# x or y
print(10 or 20)        #10
print(0 or 20)         #20
print(1 or 'abc')      #1
print(0 or 'abc')      #abc

# if x evaluates to false then result is true
# always returns boolean
# not x
print(not 20)        #False
print(not '')         #True
print(not 0)           #True
print(10 or 10/0)      #10
