#-----------------------Tuple
# Immutable :- Unable to change

t=()        # empty tuple
print('Empty Tuple:',t)
t=(10)     # to make it tuple otherwise it will behave like 'int'
print('Tuple Initialize without comma:',t)
t=(10,)     # to make it tuple otherwise it will behave like 'int'
print('Tuple Initialize:',t)
t=(10,20,30,40,10,20)
print('Tuple Initialize part II:',t)
# syntax : t= tuple(sequence)
# How to access the element of tuple
# by using indexing & slicing

# Important functions of tuple:
# 1. len(tuple): length of tuple , this is function
print('Length of tuple:',len(t))

# 2. count(x) : counting the x present in a tuple , this is method
print('Count of x in a tuple:',t.count(10))

# 3. index(x) : to get the index of x i.e. present in a tuple , this is method
print('Index of x in a tuple:',t.index(20))

# 4. sorted(tuple) : to sort the element based on natural sorting order. eg no asc , string alphabetical order
# Tuple does not have sort methodology , as tuple is immutable.
# Here in following a new list is created.
print('Sorting of a tuple:',sorted(t))   #Sorting of a tuple: [10, 10, 20, 20, 30, 40]
print('Sorting of a tuple:',tuple(sorted(t)))   #Sorting of a tuple: (10, 10, 20, 20, 30, 40)

# Sorting in reverse order
print('Sorting of a tuple in reversed order:',tuple(sorted(t,reverse=True)))   #Sorting of a tuple: (40, 30, 20, 20, 10, 10)

# 5. Min & Max function
# only for homogeneous values
print('Max value in a tuple:',max(t))
print('Min value in a tuple:',min(t))

# 6. Compare function
# cmp: only in python 2 not in python 3
# cmp(t1,t2): only in python 2 not in python 3
# can use >,<,>=,<=
t1=t
print('Copied tuple values are :',t1)
print('t1==t',t1==t)
print('t1<t',t1<t)

# 7. Tuple packing and unpacking
#packing : Grouping into single unit
a,b,c,d=10,20,30,40
t=a,b,c,d               #'This is called packing:'
print('This is called packing:',t)
# Unpacking: assigning/ungrouping tuple values to elements or variables
a,b,c,d=t               #'This is called unpacking:'
print('This is called unpacking:','a=',a,'b=',b,'c=',c,'d=',d)

# List packing & unpacking is applicable for all sequence.

#8. Tuple Comprehension  => NOT SUPPORTED
# tuple comprehension is not supported as result is type of 'generator'
# t= (exp for x in sequence if condition)
t= (x*x for x in range(1,11))
print(t)                   #  <generator object <genexpr> at 0x000001FABFB87448>
for x in t:
    print('Tuple values after tuple comprehension then looping to get values : ',x)