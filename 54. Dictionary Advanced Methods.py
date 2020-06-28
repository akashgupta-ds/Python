# ----------- Dictionary{} -----------------
# key-value pairs
# A group of values with key-value pair
# Mutable
# Dynamic ,Growable
# Key can not be duplicated , value can be duplicated
# NO order , no index applicable

# How to create dict ?
# empty dictionary
d={}
print('Empty Dictionary Created: ',d)
d=dict()
print('Empty Dictionary Created: ',d)

d[100]='Akash'
d[200]='Machine Learning'
d[300]='Python'
d[400]='Data Science'
d[500]='AI'

print('Dictionary Created: ',d)
print('Dictionary Key: 200 And Value is ',d[200])

# key error if the key is not in dictionary
#print('Dictionary Key: 600 And Value is ',d[600]) #KeyError: 600

# How to update dictionaries
# if key exists then update otherwise it will add
#d[key]= value
d[600]='Sql Server'
print('Dictionary Element Updated: ',d)

# How to delete value from dictionaries
# syntax : del[key]
del d[600]
print('Dictionary Deleted Updated: ',d)

# All clear or total value clear
d.clear()
print('Dictionary Cleared: ',d)

# Want to delete entire dictionary :
# after deletion 'd' anymore & available for Garbage collection
del d
#print('Dictionary Deleted : ',d)

# How to specify multiple values for the signle key
# using list
list=['Sachin','Dhoni','Yuvraj','Akash']
d={100:list}
print('Dictionary Cleared by using list: ',d)

# important functions
# using set of tuple in key - value pair
# using tuple of tuple in key - value pair
# using list of tuple in key - value pair
d=dict([(100,'Testing'),(200,'AKash'),(400,'Sachin')])
print('Dictionary Cleared by using list of Tuple: ',d)

#3. pop(key) : for removing the entry
d.pop(100)
print('Dictionary entry deleted: ',d)

#4. popitem() : one random key value will be removed and return
# on empty dictionary you can not perform this
d={100: 'Akash', 200: 'Machine Learning', 300: 'Python', 400: 'Data Science', 500: 'AI'}
d.popitem()
print('Dictionary entry deleted: ',d)

#5. keys(): to show all the keys in dictionary
#dict_keys([100, 200, 300, 400])
print('Show all the keys in dictionary :',d.keys())


#6. values(): to show all the values in dictionary
# dict_values(['Akash', 'Machine Learning', 'Python', 'Data Science'])
print('Show all the values in dictionary :',d.values())

#7. items(): to show all the items in dictionary
# dict_values(['Akash', 'Machine Learning', 'Python', 'Data Science'])
list=d.items()
for k,v in d.items():
    print('Key',k,'Value',v)


#8. copy(): to clone or duplicate

d1=d.copy()
print('Show all the values in dictionary after copy method:',d)

#9. setdefault(k,v): if the key is available then replace with this key and new value
# d[key]=value
d.setdefault(500,'Sql Server')
print('Show all the values in dictionary after setdefault method:',d)

#10. update: if the key is available then replace with this key and new value
# d[key]=value
d1={'a':'apple','b':'banana','c':'cat'}
d.update(d1)
print('Show all the values in dictionary after update method:',d)

# if key does not exist then None will return.
print('Show all the values with get method in dictionary after update method:',d.get(106))

#11. Dictionary Comprehension:
# squares={key:value for x in sequence if condition}
d2={x:x**2 for x in range(1,20)}
print('Show all the values in dictionary after comprehension:',d2)
