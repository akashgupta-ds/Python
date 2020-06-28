#-------------Dictionary{} data type------------------
# Key - Value pair
# Duplicates keys are not allowed
# Duplicates values are allowed
# Growable in nature
# Dictionary by default is mutable
# key can be any type of object
# value can be any type of object

# How to create empty dictionary and set

# empty set
s=set()
print(type(s))                  #<class 'set'>
# empty dictionary
d={}
print(type(d))                  #<class 'dict'>

d={100:'akash',200:'abc',300:'def'}
print(type(d))                  #<class 'dict'>

# Growable
d[400]='Science'
print(d)

d[500]="Sports"
print(d)

# If the key is already exists, old value will be replaced with same key ...otherwise will add a new Key Value pair
d[500]="Hockey"
print(d)
