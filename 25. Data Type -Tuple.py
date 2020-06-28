#-------- Tuple() -----------------------------
# 1. Insertion order is preserved and duplicates are allowed
# 2. Hetrogeneous object/order is allowed
# 3. Growable : Increasing and reducing operation
# 4. IMMutable : Do not update and remove the elements [Not applicable - append,remove,assign...]

# 1. Insertion order is preserved and duplicates are allowed

t=(10,20,30,40)
print(type(t))              # <class 'list'>
print(t)

# 2. Hetrogeneous object/order is allowed
t=(10,20,30,40,'Akash',True)
print(t)            #(10, 20, 30, 200, 'Akash')

# None is like and object value
#t.append(None)      #AttributeError: 'tuple' object has no attribute 'append'
print(t)
print(t[0])
print(t[-1])        #None
print(t)
print(t[1:5])       #(20, 30, 200, 'Akash')
print(t[-5:-1])     #(20, 30, 200, 'Akash')
print(t[-5:0])      #()
print(t[-5:])      #(20, 30, 200, 'Akash', None)
print(t[:-1])      #(20, 30, 200, 'Akash', None)

# 3. Growable : Increasing and reducing operation

#t.remove(None)      # removed None from list (10, 20, 30, 200, 'Akash')
print(t)

# IMMMUTABLE in nature
#t[0] = 100          #error  TypeError: 'tuple' object does not support item assignment
# REPEATATION OPERATOR it works
t1=t*2             #(10, 20, 30, 200, 'Akash', None, 10, 20, 30, 200, 'Akash', None)
print(t1)

t2=(10,20,[30,50])  # list object exists internally in this example.
print(t2)