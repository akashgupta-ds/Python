# -----------------Generator Function----------------------------
# To generate sequence of values.
# This is responsible to generate sequence of values
# yield keyword
# Biggest benefit : due to generator is memory utilization as compared to list or other sequence
# tuple comprehension is not applicable and it will be type of <generator>
# internally tuple comprehension take care yield keyword
# Advantages:
# memory utilization
# performance improvement
# helpful in reading the huge number of data
# compared to normal iterators generators are easy to use.
# Generators are best suitable for web scrapping.


def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g=mygen()
print(type(g))
print(type(g)) # A
print(next(g)) # B
print(next(g)) # C
#print(next(g)) # value error

# Biggest benefit : due to generator is memory utilization as compared to list or other sequence
# tuple comprehension is not applicable and it will be type of <generator>
l=[x*x for x in range(1000000)]  #memory error if put 100000000000000000000
print('Without Generator :',l)

# internally tuple comprehension take care yield keyword
g=(x*x for x in range(1000))  #range(10000000000000000) )
try:
    while True:
        print('Generator:',next(g))         # no memory error
except StopIteration:
        pass


import time
def countdown(num):
    print('Countdown starting...')
    while num>0:
        yield num
        num=num-1
values=countdown(10)
for x in values:
    print(x)
    time.sleep(1)

