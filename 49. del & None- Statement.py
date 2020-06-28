#----------------del statement--------------
# del is keyword in python for managing memory.
# Garbage collector works with 'del'.
# this will delete the variable
# if the variable is no more needed then we can delete the variable
# it improves the memory utilization by defualt improved
# del x
s1="Akash"
s2="Gupta"
print(s1)
#del(s1)         # deleted s1 variable
print(s1)       # NameError: name 's1' is not defined


# del Vs None
# if we require the variable and object then use 'None'
# However, if  we don't require variable or object then use 'del'
# if multiple object reference one variable then if delete one object then only one object effected
del s2
y=None
s1='Test'
s2='Test'
s3='Test'
del s1
#print(s1)       #NameError: name 's1' is not defined
print(s2)
print(s3)

