#------------------eval input
# eval ()
# always takes input as string and result will be evaluated correspondigly
# whatever the data we provide it eval converts internally to that data type
# eg. tuple to tuple,list to list


x=eval('10+20+30')
print(x)    #60

#y=eval("Read the list")
#print(type(x))

x=eval(input('Enter a list :'))
print(x)

a,b,c =[eval(x) for x in input('Enter 3 values : ').split(',')]
print(type(a))        #  <class 'int'>
print(type(b))        #  <class 'int'>
print(type(c))        #  <class 'int'>