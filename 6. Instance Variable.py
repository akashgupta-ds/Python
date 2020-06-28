#Types of Variable
#1. Instance Variable
#2. Static Variable
#3. Local Variable
# If the value of the variable varied from object to object then it is called instance vairable.
# For every object a separate copy of instance variable is created.
# Instance variable should be created under constructor using self.
# When we can declare instance variable
# 1. Inside constructor by using self
# 2. Inside instance method by using self
# 3. From outside of the class by using object reference.

# How to access instance Variable:
# 1. within the class by using self
# 2. outside of the class by using object reference

# How to delete instance variable:
# 1. del self.variablename -----INSIDE CLASS
# 2. del objectreference.variablename -------OUTSIDE CLASS


class instanceClass:
    #constructor with instance variable for initialization
    #
    def __init__(self,solarsys,country,city):
        self.solarsys=solarsys
        self.country=country
        self.city=city

    #instance method
    def methodName(self):
        # How to access instance Variable:
        print("Solar System Name is :", self.solarsys)
        print("Which country do you want to find yourself:", self.country)
        print("Which city do you want to find yourself:", self.city)

    # instance methods
    def fact(self,num):
        #factorial=0
        if num <= 1:
            return 1
        else:
            return num * fact(num-1)

    #class method declaration for fibonacci series
    @classmethod
    def fibonacci(cls, nthinput):
        count = 0
        n1,n2 = 0,1
        while count <= nthinput:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count+=1



# Function creation
def fact(num):
    #factorial=0
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)
    #return fact(num)
    #    print('Factorial of number is:',)

objSolar=instanceClass('Venus','UK','London')
# How to access instance Variable:
objSolar.methodName()
print(fact(5))
print(objSolar.fact(5))

instanceClass.fibonacci(5)

#del objSolar.city
##Deleted instance variable city and is not accessable after this point
objSolar.methodName()
print(objSolar.city)