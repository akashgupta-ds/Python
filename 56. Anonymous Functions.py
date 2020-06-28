# -------------------Anonymous functions
# 1. without name ....nameless functions
# 2. instant usage (only one time usage)

# comparison between normal and anonymous function
# normal function
def squareIt(n):
    return n*n

print('Square of function with traditional function:',squareIt(99))
s=lambda n:n*n
print('Square of function with lambda or anonymous function:',s(99))

# syntax :
# lambda input : expression
s=lambda a,b:a+b
print('The sum of two numbers is :',s(3000,8792332))
