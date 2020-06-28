# -------------------Set---------------------
# 1. Duplicates are not allowed
# 2. Insertion order is not applicable
# 3. Hetrogenous objects are allowed
# 4. Indexing is not applicable
# 5. Mutable
# 6. Can apply mathematical operations

s={10,20,30}
#Indexing is not applicable
#print('Printing set with indexing :',s[0])  #TypeError: 'set' object is not subscriptable

s={25,35,45,89,89,90,23}
print('Duplicates are not allowed :',s)   # 89 removed
print('Set Type :',type(s))   # <class 'set'>

# Internally some hash set mechanism is working
# slicing is not applicable in set

#print('Slicing is not applicable :',s[1:7]) #TypeError: 'set' object is not subscriptable

# 1. List in to set
# syntax : s=set(list)
s=set([25,35,45,89,89,90,23,700,900,1000])
print('List converted to set as :',s)

# for creating empty set
s=set()                  # creates empty set
print('Empty Set :',s,'And Type is :',type(s))
#Empty Set : set() And Type is : <class 'set'>

# if created as following then
s={}
print('Empty Set :',s,'And Type is :',type(s))  # creates empty dictionary
#Empty Set : {} And Type is : <class 'dict'>

#2. How to add or update set
# s.add(new element) , s.update(sequence)=> sequence is list,set, tuple
s=set()
# add(new element) method=takes only one arguement
s.add(20)
print('Add method to set as :',s)

s.add(10)
print('Add method to set as :',s)

# update(sequence) method with List
s.update([10,20,30,89,90,100])
print('update method to set as :',s)
# update(sequence) method with tuple : duplicates removed
s.update((101,201,301,891,901,1001))
print('update method to set as :',s)
# update(sequence) method with dictionary : only key added
s.update({1011:2011})
print('update method with dictionary as :',s)

# copy() - method to copy set from other set
# different reference address allocated after copy

s1=s.copy()     # copy
print('Copy method to clone the set :',s1,'With Address id:',id(s1))

s2=s            # aliasing
print('Aliasing method to clone the set :',s2,'With Address id:',id(s2))

# pop() -
# remove and return the element
# some random element will be removed
# a group of mobile numbers

s3={10,30,40,60,80,90}
print('Pop any random element :',s3.pop(),'Now the set :',s3)

# if an empty set then 'keyerror' by default we will get.
s4=set()
#print('Pop any random element :',s4.pop(),'Now the set :',s4) #KeyError: 'pop from an empty set'

# 5. remove(x) : Remove the specified element
# if the element which is to remove, is not available then this method raise the error.
print('Remove method for removing element :',s3.remove(10),'Set now :',s3) #KeyError: 100

# 6. discard(x): Remove the specified element
# # if the element which is to remove, is not available then this method will not raise the error.
print('Remove method for removing element :',s3.discard(100),'Set now :',s3)

# 7. clear(): clear the entire set and returns empty set
print('Clear method :',s3.clear(),'Set now :',s3)

# Mathematmical operations:
# Union : s1.union(s2) => s1 U s2
print('Union method for two sets :',s1.union(s2))

# intersection : s1.intersection(s2) => s1 & s2
print('intersection method for two sets :',s1.intersection(s2))

# symmetric_difference : s1.symmetric_difference(s2) => s1 & s2
print('symmetric_difference method for two sets :',s1.symmetric_difference(s2))

# set comprehension
# syntax s={expression for x in sequence if condition}
s={x*x for x in range(1,6)}
print('Set is:',s)

# To eliminate duplicate values

