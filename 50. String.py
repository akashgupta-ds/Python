#--------------------String
# ''' ''' for multiline
# \' for single quote in sentence/string or in enclosed sentence we use single quotes
s='''For 
        Multiline'''
print(s)
s='This is \' single quote symbol'
print(s)

# how to access character of string
# by using index
# by using slice operator

s=input('Enter some string : ')
i=0
for x in s:
    print('The character present at :{} and is : {}'.format(i,i-len(s),x))
    i=i+1
# Membership operator
# in

s="akash"
print('a' in s)
print('z' in s)

s= input("Enter Main string : ")
subs=input('Enter substring to search:')
if subs in s :
    print('subs, is found in main string')
else:
    print('subs, is not found in main string')

# lstrip():left space removal
# rstrip():right space removal
# strip(): left and right extra spaces removal

print(s.strip())
# counting substrings in string method.
# syntax : s.count(substring,beginindex ,endindex)
s='Machine Learning'
print(s.count('Mach'))

# replacing a string with another string
# syntax; s.replace('old string','new string')

s=s.replace('Machine','Python')
print(s)

# String is immutable then how can you change string
#Ans: s object does not change . however a new object created to accomodate the changes of .replace()
s1=s.replace('a','b')
print(id(s))
print(id(s1))
print(s1)

# splitting of strings :
s=s.split('Saperator') # default is space

s='Python Learning'
l=s.split()     # after split assign it to list
print(l)
for x in l:
    print(x)

# rsplit : Reverse split
# rsplit(saperator,max,split)
# max is maximum number of split ..so if max=3 then total number of parts 4
s='20,23,4534,56456,6754,23432,465452,341,3,6,6,7,9'
l=s.split(',',3)
print(l)
l=s.rsplit(',',3)
print(l)

# join()
# syntax :s=separtor.join(list)
l=['Python', 'Learning','Machine','Power Bi']
s='-'.join(l)
print(s)

# with tuple
t=('Python', 'Learning','Machine','Power Bi')
s='-'.join(t)
print(s)

# changing case of a string
#upper()= To convert to upper case
#lower()= To convert to lower case
#swapcase()= To convert to opposite case i.e. upper to lower and vice versa
#title()= To convert to title case
#Capitalize()= To convert only first lette in upper case
s.upper()
s.lower()
s.swapcase()
s.title()
s.capitalize()

print('UPPER CASE:',s.upper())
print('Lower CASE:',s.lower())
print('Swap CASE:',s.swapcase())
print('Title CASE:',s.title())
print('Capitalize CASE:',s.capitalize())

# checking starting of strings.

print(s.startswith('Python'))

# checking ending of strings.
print(s.endswith('Bi'))