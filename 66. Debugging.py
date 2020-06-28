#-----------------------Debugging-------------
# defect/bug: mismatch between expected result and actual result
# the process of identifying and fixing bug is called debugging

def squareit(x):
    return 2*x

# how to debug the program
# use print('Hello') statement for debugging
# by using assert statement for debugging purpose
# like print()

# Type of assert
#1. Simple version
#2. very simple version (Augmented version)

# assert x
# assert y
# After fixing the problem these assert statement does not execute at client machine
# you can enable and diable assert statement
# after fixing the bug , print () statement should be removed

# Simple version:
# assert contional_expression
# assert error

x=10
assert x==10
assert x>10
print(x)

# Augmented version : with message
# assert conditional_expression, message

assert x>10,'Here x values should be >10 but it is not'