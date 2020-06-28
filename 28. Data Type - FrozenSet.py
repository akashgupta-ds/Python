#----------Frozenset() Data Type------------------------
# List Vs Set
# if you don't want order and duplicate items then choose set.
# Denoted by {}
# Insertion order not preserved.
# Duplicates are not allowed. [Group of Unique values]
# Indexing does not support
# Heterogeneous objects are allowed
# frozenset is immutable
# Growable in nature
# how to create empty set s=set()

s={10,20,30,10,20,30}
fs=frozenset(s)
print(fs)            # removed duplicates
print(type(fs))      # <class 'frozenset'> removed duplicates
#print(s[0])         # Indexing does not support TypeError: 'set' object is not subscriptable
#print(s[1:])        # Does not support slicing

#fs.add('akash')      # not growable in nature
#print(fs)
#fs.remove(10)        # frozenset is immutable
#print(fs)