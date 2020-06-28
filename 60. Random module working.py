#-------------random module working-----------------
# random(): generates random values between 0&1 (float) except 0& 1
# 0<x<1

from random import *
# 1. random():
for i in range(10):
    print('random function for :',random())  # for generating random float values between 0 & 1

# 2. randint(x,y):for generating random int values between x & y (inclusive)
for i in range(10):
    print('randint function for :',randint(1,1000))  # for generating random int values between x & y (inclusive)


# 3. uniform(): always generates float values between x & y , not inclusive
for i in range(20):
    print('uniform function for :',uniform(1,1000))  # always generates float values between x & y , not inclusive

# 4. randrange(start,stop,step): always generates/returns a random number with in a range with step.
# excluding start and stop
# start < x < stop
for i in range(10):
    print('randrange function for :',randrange(10))  # always returns a random number with in a range with step.
    print('randrange function for :', randrange(1,11))  # always returns a random number with in a range with step.
    print('randrange function for :',randrange(1, 1000, 15))  # always returns a random number with in a range with step.

# 5. choice(): random object from the sequence. (Indexable collection) eg. list ,tuple etc.
list=['US','UK','Russia','India','Japan','Germany','Scotland']
for i in range(10):
    print('Choice function for :',choice(list))  # always generates float values between x & y , not inclusive