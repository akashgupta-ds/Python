# ---------------Command line arguments--------------
# argv=> list type => argument values
# module : sys
# import :sys
# argv[begin:end:step] Based on index values

from sys import argv
l=[10,20,30,40,50,60,70]
argv=l
print(type(argv))
print((argv[1:]))
print((argv[0]))
print((argv[1]))

# is there any way to print all the element by stepping only middle element from the array?

print('The no of command line args :', len(argv))
print('The list of command line args :', (argv))
print('The command line args one by one :')
for x in argv:
    print(x)

print('Slice operator result :', argv[1:6])

# Read a group of int values from the keyboard as cmd line arg and print sum

args=argv[1:]
sum=0
for x in args:
    n=int(x)
    sum=sum+n
print('The sum is :',sum)

# for passing one command line arg. use quotes

print(args[0] + args[1])
print(argv[0] + argv[1])