#------------------List[] Data Type---------------
# 1. Insertion order is preserved and duplicates are allowed
# 2. Hetrogeneous object/order is allowed
# 3. Growable : Increasing and reducing operation
# 4. Mutable : Do update and remove the elements [append,remove,assign...]

# 1. Insertion order is preserved and duplicates are allowed

l=[]
print(type(l))              # <class 'list'>
l.append(10)
l.append(20)
l.append(30)
l.append(200)
print(l)


# 2. Hetrogeneous object/order is allowed
l.append('Akash')
print(l)            #[10, 20, 30, 200, 'Akash']
# None is like and object value
l.append(None)
print(l)
print(l[0])
print(l[-1])        #None
print(l)
print(l[1:5])       #[20, 30, 200, 'Akash']
print(l[-5:-1])     #[20, 30, 200, 'Akash']
print(l[-5:0])      #[]
print(l[-5:])      #[20, 30, 200, 'Akash', None]
print(l[:-1])      #[20, 30, 200, 'Akash', None]
# 3. Growable : Increasing and reducing operation
# MUTABLE in nature
l.remove(None)      # removed None from list [10, 20, 30, 200, 'Akash']
print(l)


# REPEATATION OPERATOR
l1=l*2             #[10, 20, 30, 200, 'Akash', None, 10, 20, 30, 200, 'Akash', None]
print(l1)