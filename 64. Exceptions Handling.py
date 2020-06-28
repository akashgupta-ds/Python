# -----------------------------Exception Handling-------------------
# Rules:
# 1. try without except or finally is always invalid
# 2. without try except is always invalid
# 3. per try only one else and finally is allowed. However multiple except allowed.
# 4. Between try & except there should be no independent statement to discontinue the continuity.
# 5. finally without try is always invalid.
# 6. we can take multiple except blocks for the same try but we can not take multiple else & finally.
# 7. else without except is invalid.
# 8. we can take try-except-finally in try
# 9. try-except-finally order is important
# 10. Nesting of try - except - else - finally is possible.

# Types of exceptions.
# Predefined exception / in built exception
# Userdefined exception/ customized exception

# 1. Predefined exception / in built exception
# The exception which are raised automatically by python whenever a particular event occurs....
# eg1. print(10/0)
# print(10/0)
# eg2. print(int('ten')) # value error

# 2. Userdefined exception/customized exceptions:
# exception handler developed by developer as per program
# insufficientfundsexception
# invalidcouponcodeexception

# How to define and raise customized exceptions:
#
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input('Enter age:'))
if age>60:
    raise TooOldException('Too Old Exception raised')
elif age<18:
    raise TooYoungException('Too Young Exception raised')
else:
    print('Thanks')
