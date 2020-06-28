#------Print form-----------------------
# form1 : Without parameter

print('Hello')

# form2 :
# + => both arguemnts should be str type only
# * => both arguemnts should be str type other should be int

print('Hello ' + 'World') #
print('Hello ' * 3) #
print('Hello ','Software') #

# form3:
# print() with variable number of arguments
# , helps to put one space between arguments
a,b,c=10,20,30
print('The values are :',a,b,c)

# sep attribute => separator attribute
# default value sep=> space
# sep=' '
print(a,b,c)
print(a,b,c,sep=',')
print(a,b,c,sep=':')


# print with end attribute :
# end=' '
# by default print() print new line
print('Hello')
print('World')
print('Hello','World',end=' ')
print('with Smile :)')

# By using end='  ' subsequent print will concatenated.
# default value end => new line \n

l=[10,20,30,40]
t=(10,20,30,40)
s={10,20,30,40}

print(l)
print(t)
print(s)

print(l,end='.')
print(t,end='.')
print(s)
print(l,t,s)

# print formatted string
# % i => int type
# % d => int type
# % f => float type
# % s => str type

# syntax
#print('formatted string '%(variable list))

a,b,c=10,20,30
print('a value is % i ' %a)
print('a value is %i and b value is %i'%(a,b))

a='Akash'
b=[10,20,30]
print('Hello %s the list is :%s '%(a,b))

# print() with replacement operator :{ index no}
name='Akash'
salary=10000
city='London'
#1
print('Hello {0} your salary is {1} and your city is {2} '.format(name,salary,city))
#2
print('Hello {} your salary is {} and your city is {} '.format(name,salary,city))
#3
print('Hello {x} your salary is {y} and your city is {z} '.format(x=name,y=salary,z=city))  # order can be changed
