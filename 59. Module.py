# -----------------------Module----------------------------------
# Several variables, functions , classes in a single python file is called as module e.g. math.py
# Code reusability
# A group of functions and variables saved to a file
# length of the code will be reduced and readability
# Maintainability
# help(modulename)
# syntax:
# import module
# import module1,module2,module3

# Reloading a module
# PYC=> __pycache__ location for pyc file
# module loads only one time however try to import more than one time
# if the module is updated outside then updated copy is not avilable
# so by using 'imp' module ,reload function we can overcome this problem
# updated version of module is not available by default use reload(module)
# dynamic modules : coupon codes.

# -----------------------Package----------------------------------
# A group of modules is called as package

# -----------------------Library----------------------------------
# A group of packages is called library

# -----------------------special variable __name__----------------------------------
# __cached__
# __doc__
# __name__
# __builtins__
# __file__
# private variable (highly private)

import math
import numpy as np
import time
import emp
from importlib import reload

#print(emp(1,'Test','test','test add').dispay())
print(dir(emp))
time.sleep(30)
print('After sleeping time :')
import Module1
reload(Module1)
print('This is last line of program')
# updated version of module1 is not available by default.
print(math.factorial(10))

print(Module1.f1())

# module functionality can be executed directly or indirectly
def f1():
    if __name__=='__main__':
        print('The code executed directly as a program')
        print('The value of __name__.',__name__)
    else:
        print('Indirectly')
        print('The value of __name__.', __name__)
