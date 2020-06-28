# ------------------Data type----------------
# int , float, complex , bool , str are all fundamental datatype. All data types are 'IMMUTABLE'
# There is no 'char' datatype in Python , It shows only with 'str'
# long is not available in python 2.0 and python 3.0

# Type casting or type coersion
print('Int Datatype Conversion Start')
# -----------------int()-----------------
# Converting different datatype variables to int using int()
a=int(12345)
print(a)
a=int(True)
print(a)
#a=int(10+20j)  # TypeError: can't convert complex to int
print(a)
#a=int("10.5")  # ValueError: invalid literal for int() with base 10: '10.5'
a=int("1111")
print(a)
#a=int("0B1111") # ValueError: invalid literal for int() with base 10: '0B1111'
#print(a)
# -----------------INT-----------------
print('INT Datatype Conversion end')

print('Float Datatype Conversion Start')
# -----------------float()---------------
# Converting different datatype variables to float using float()
a=float(10)
print(a)          # 10.0
#a=float(10+20j)  # TypeError: can't convert complex to float
print(a)
a=float(True)     # 1.0
print(a)
a=float(False)    # 0.0
print(a)
a=float("10")    # 10.0
print(a)
a=float("10.5")    # 10.5
print(a)
#a=float("ten")    # ValueError: could not convert string to float: 'ten'
#print(a)
#a=float("0b1111")   # ValueError: could not convert string to float: '0b1111'
#print(a)
# -----------------float()---------------
print('float Datatype Conversion End')

# -----------------complex()---------------
# Converting different datatype variables to complex using complex()
# Complex() :- Other types to complex types
# form-1 : complex(x) => x+0j
# form-2 : complex(x,y) => x+yj
# x=> real part
# y=> imaginary part
# complex(x,y) => it is overloaded function

print('Complex Datatype Conversion')
a=complex(10)
print(a)          # 10.0
a=complex(10+20j)
print(a)
a=complex(True)     # 1.0
print(a)
a=complex(False)    # 0.0
print(a)
a=complex("10")    # 10.0
print(a)
a=complex("10.5")    # 10.5
print(a)
#a=complex("ten")    # ValueError: complex() arg is a malformed string
#print(a)
#a=complex("0b1111")   # ValueError: complex() arg is a malformed string
#print(a)

# form-2 => complex(x,y)=> x+yj
a=complex(10,20)   # 10+20j
print(a)
a=complex(True,False)   # (1+0j)
print(a)
a=complex(10,20.5)   # (10+20.5j)
print(a)
#a=complex("10","20.5")   # TypeError: complex() can't take second arg if first is a string
#print(a)
# can't take second argument if first is a string
print('Complex Datatype Conversion End')

print('Bool Datatype Conversion Start')
# -----------------bool()---------------
# Converting different datatype variables to bool using bool()
a=bool(10)
print(a)          # True
a=bool(10+20j)    # True
print(a)
a=bool(True)     # True
print(a)
a=bool(False)    # False
print(a)
a=bool("10")    # True
print(a)
a=bool("10.5")    # True
print(a)
a=bool("ten")    # True
print(a)
a=bool("0b1111")   # True
print(a)
a=bool("")      # False
print(a)
a=bool(" ")     # True
print(a)
# -----------------bool()---------------
print('Bool Datatype Conversion End')


print('Str Datatype Conversion Start')
# -----------------str()---------------
# Converting different datatype variables to str using str()
a=str(10)
print(a)          # 10
a=str(10+20j)    # 10+20j
print(a)
a=str(True)     # True
print(a)
a=str(False)    # False
print(a)
a=str("10")    # 10
print(a)
a=str("10.5")    # 10.5
print(a)
a=str("ten")    # ten
print(a)
a=str("0b1111")   # 0b1111
print(a)
a=str("")      # ""
print(a)
a=str(" ")     # " "
print(a)
# -----------------Str()---------------
print('Str Datatype Conversion End')


print('bytes Datatype Conversion Start')
# -----------------byte()---------------
# Converting different datatype variables to bytes using bytes()
# it represent a group of byte just like an array
# in the range 0 to 256 [ Throw error if outside of the range]
# immutable

a=bytes(10)
print(a)          # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

x=[10,20,30,40,50]
j=0
b=bytes(x)
print(b)            # b'\n\x14\x1e(2'
print(type(b))      # <class 'bytes'>
for i in b:
    print('Print byte {} of {}:'.format(i,bytes(i)))
print(b[0])         # 10
print(b[1])         # 20
print(b[-1])         # 50
print(b[0:3])         # 50

for x in b:
    print(x)
#b[0]=120        # throw error as it is immutable

#print(b[0])     #TypeError: 'bytes' object does not support item assignment
# -----------------byte()---------------
print('bytes Datatype Conversion End')

print('bytearray Datatype Conversion Start')
# -----------------byte()---------------
# Converting different datatype variables to bytearray using bytearray()
# it represent a group of byte just like an array
# in the range 0 to 256 [ Throw error if outside of the range]
# mutable

a = bytearray(10)
print(a)  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

x = [10, 20, 30, 40, 50]
b = bytearray(x)
print(b)  # bytearray(b'\n\x14\x1e(2')
print(type(b))  # <class 'bytearray'>
b[0]=120
for i in b:
    print('Print bytearray {} of {}:'.format(i,bytearray(i)))

# b[0]=256     # ValueError: byte must be in range(0, 256)
b[0]=255     # ValueError: byte must be in range(0, 256)
print(b[0])  # 10
print(b[1])  # 20
print(b[-1])  # 50
print(b[0:3])  # 50

for x in b:
    print(x)
# b[0]=120        # throw error as it is immutable

# print(b[0])     #TypeError: 'bytes' object does not support item assignment
# -----------------byte()---------------
print('bytearray Datatype Conversion End')
