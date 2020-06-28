#----------__init__(self)-------------------------
# The name of constructor is always __init__()
# The MAIN OBJECTIVE of Constructor is to declare and initialization of the instance variables*
# Whenever we are creating object, constructor will be called automatically
# And we don't need to call it explicitly
# For every object, Constructor will only be Executed ONLY ONCE.
# For every Constructor atleast one Arguement is Compulsory.
# __init__ CAN'T BE CHANGE
# PYTHON will provide default constructor if not defined
# Constructor overloading does not require in python due to DYNAMIC Data TYPE
# For Overloading there should be different data type argument passed in methods
# Constructor overloading easily acheivable through * args
# Always last constructor will be applicable for instance variable declaration and Initialization


class Test:
    '''constructor overloading does not require in python'''
    '''constructor overloading easily acheivable through * args '''
    def __init__(self):
        print('No-Arguements')

    def __init__(self,x):
        print('One Arguement')

    '''Always last constructor will be applicable for instance variable declaration
        and Initialization
     '''
    def __init__(self,x,y):
        print('Two Arguements')
    # def __init__(self):
    #     print('No-Arguements')
obj=Test(10,20)
# obj=Test()
print(obj)