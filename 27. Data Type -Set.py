#----------Set{} Data Type------------------------
# List Vs Set
# if you don't want order and duplicate items then choose set.
# Denoted by {}
# Insertion order not preserved.
# Duplicates are not allowed. [Group of Unique values]
# Indexing does not support
# Heterogeneous objects are allowed
# Set is mutable
# Growable in nature
# how to create empty set s=set()

s={10,20,30,10,20,30}
print(s)            # removed duplicates
#print(s[0])         # Indexing does not support TypeError: 'set' object is not subscriptable
#print(s[1:])        # Does not support slicing

s.add('akash')      # Heterogeneous objects are allowed
print(s)
s.remove(10)        # Set is mutable
print(s)