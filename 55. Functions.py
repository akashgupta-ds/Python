# ---------------------Functions---------------------
# Defined outside of the class
# Code reusability
# code optimization
# time reducing
# Define outside of the class
#
def fucntionName():
    x=0
    print('Method/Function')
    return x

# Parameter types
#   1. Positional
#   2. Keyword
#   3. default
#   4. var

# Default return values is 'None'

# 1. Positional arguments :
# returns multiple values and can assign to tuple as well
# No. of arguments are important
# a,b are positional arguments
# on changing the order the result could change
# order should be preserved

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
# assign to tuple
t=a,b,c,d=calc(10,50)
print('Function result for Positional Arguments is :',t)

# 2. Keyword arguments
# order is not important
# a,b are keyword arguments
# Default argument should be at last
t=calc(a=100,b=50)
print('With right order keyword arguments :',t)

t=calc(b=50,a=100)
print('With switched order keyword arguments :',t)

t=calc(100,b=50) # valid
print('With first positional argument at first  keyword arguments:',t)

#t=calc(b=100,500) # invalid
#print('With first positional argument at last :',t)
#t=calc(100,a=500) # invalid
#print('With second positional argument at first :',t)

# 3. Default argument
# default parameter should be at last
# name is a default argument
#def wish(name='Guest',msg): # error
#    pass
def wish(msg,name='Guest'):
    print(name,':',msg)
    pass

print(wish('Testing Default argument'))

# 4. variable lenght arguments : 'var'
# if we want to change the number of arguments
# any number of arguments
# n=> tuple
# positional argument should be first defined then keywork arguments
def sum(*n):
    result=0
    for x in n:
        result=result+x
    print('Var arg. Function,The sum is :',result)
    return result

print('The sum of numbers are :',sum(10))

print('The sum of numbers are :',sum(10,20))
print('The sum of numbers are :',sum(10,20,30))

# 2. Keyword arguments-**kwargs
# dictionary type
# keyword variable argument

def display(**kwargs):
    print('Record Information:')
    for k,v in kwargs.items():
        print(k,v)

display(name='D',marks='100',age=48,GF='5')
display(name='A',marks='300',brand='Gucci')

# keyword variable length arguments
# arg1 & arg2: positional arg
# arg3 & arg4 : Default arg
def func(arg1,arg2,arg3=4,arg4=8):
    print('arg1=',arg1,'arg2=',arg2,'arg3=',arg3,'arg4=',arg4)

func(25,50,arg4=100) # valid o/p arg1= 25 arg2= 50 arg3= 4 arg4= 100
func(arg4=100,arg1=3,arg2=4) # valid o/p arg1= 3 arg2= 4 arg3= 4 arg4= 100
#func(arg3=100,arg4=40,20,30) # SyntaxError: positional argument follows keyword argument
#func(20,30,arg2=100,arg3=3) # TypeError: func() got multiple values for argument 'arg2'
#func(4,5,arg3=100,arg5=3) # TypeError: func() got an unexpected keyword argument 'arg5'