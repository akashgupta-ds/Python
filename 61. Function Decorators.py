# ---------------------Function Decorator ---------------------
# Bride => Beautiparlour => heroine
# input function => decorator => output function
# Decorator is itself a function
# input function => decorator function => output function with external functionality
# 1. Without modifying the existing functions functionality, extending the extra feature is called decorator
# 2. Through decorator function we pass the function name for which we require to extend the functionality as argument
# 3. decorator annotation . name of the extended function
# 4. the decorator acts like a wrapper
# 5. The decorator for function with a name of parameters/arguments.
# 6. In this way, 'args' will be the tuple of the positional arguments and 'kwargs' will be the dictionary of keyword
# arg.


# extending the functionality of wish(name) function by decor function decorator
def decor(func):
    def inner(name):
        if name=='sunny':
            print('Hello Sunny bad morning')
        else:
            func(name)
    return inner        # returning function as output

@decor
def wish(name):
    print('Hello',name,'Good Morning')

# with decor function
wish('Akash')           # o/p Hello Akash Good Morning
wish('sunny')
wish('Ravi')

decorfunction=decor(wish)
wish('sunny')
decorfunction('sunny')



#--------------------------------Chaining decorators----------------------------------
# 1. Multiple decorator can be chained in python.
# 2. This is to say, a function can be decorated multiple times with different (or same) decorators. We simply
# place the decorator above the desired function

def works_for_all(func):
    def inner(*args,**kwargs):
        print('I can decorate any function')
        return func(*args,**kwargs)
    return inner

def star(func):
    def inner(*args,**kwargs):
        print('*','I can decorate any function * 30')
        func(*args,**kwargs)
        print('*',30)
    return inner

def percent(func):
    def inner(*args,**kwargs):
        print('%','I can decorate any function % 30')
        func(*args,**kwargs)
        print('%',30)
    return inner

# decorator chaining
@star
@percent
def printer(msg):
    print(msg)

printer('Hello Decorator')
