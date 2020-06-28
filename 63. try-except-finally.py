#-------------------------try-except-finally----------------------------
# finally - this block always executes
# except - This block executes when an exception comes
# if inner except block does not match then it will goes to outer except block before inner finally block
# if both inner & outer except block does not match then inner finally & outer finally block. i.e. mandatory
# exception can be raise in except & finally block as well

# else block: if there is no exception in try block then else block will be executed.
# Else except block will be executed.


# Nested try-except-finally

try:
    print('outer try block')
    try:
        print('inner try block')
        print(10/0)
    except ZeroDivisionError:
        print('inner exception')
    # else block: if there is no exception in try block then else block will be executed.
    # Else except block will be executed.
    else:
        print('If no exception in inner try')
    finally:
        print('inner finally block')

except:
    print('Outer except block')
# else block: if there is no exception in try block then else block will be executed.
# Else except block will be executed.
else:
    print('If no exception in outer try')
finally:
    print('Outer finally block')
