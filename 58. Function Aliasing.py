#-----------------------------function aliasing-----------
# For the existing function , we can give another name , which is nothing but function aliasing
# Why we should use?
# when we import any module or package we can use function aliasing for using in our code
# We can also use this for system functions or module.
# This helps to abbreviate the name.

import numpy as np # np as aliasing
def adding(a,b):
    return a+b

add=adding
print(add(120,10))

ty=type
a=0
print(ty(a))
