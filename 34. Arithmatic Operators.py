# ----------------Operators------------------
# 1. Arithmatic Operators
# 2. Relational or Comparison Operators
# 3. Logical Operators
# 4. Bitwise Operators
# 5. Assignment Operators
# 6. Special Operators

# 1. Arithmatic Operators
# // => floor division operator
# +  => addition
# -  => substraction
# *  => Multiplication
# /  => divisional
# %  => Modulo operator
# **  => exponent operator or power operator

a=10
b=2

print("a+b",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)           # always return floating point value
print("a%b",a%b)
print("a//b",a//b)         # for int then int otherwise for float then float
print("a**b",a**b)

# + operator is applicable for str type
# string concatenation operator

#print('akash'+3)        #TypeError: can only concatenate str (not "int") to str
#print(3+ 'akash')        #TypeError: can only concatenate str (not "int") to str

print('akash'+ str(3))        #for concatenation both variable should be string
print('akash \t'*3)              # repeatation operator
#print('akash \t' * '3')              # TypeError: can't multiply sequence by non-int of type 'str'

#print (2** 'akash')         #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
print (10 ** -2)         #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
#print (10 / 0)         #    ZeroDivisionError: division by zero
#print(10%0)             #ZeroDivisionError: integer division or modulo by zero

