#Types of Variable
#2. Static Variable
# If the value of the variable fixed from object to object then it is called static vairable.
# Only one copy of static variable, created for every object.
# Static variable created in the class and outside of any function and constructor

# Where we can declare static variable
# 1. Within the class directly but outside of any method
# 2. Inside constructor by using class name
# 3. Inside instance method by using class Name
# 4. Inside class method by using "cls" variable name or "class name"
# 5. Inside static method by using classname
# 6. From outside of the class by using classname

# How to access instance Variable:
# 1. within the class by using classname, but inside classmethod we can also use cls method.
# 2. outside of the class by using object reference
# 3. Within the class => classname,self,cls
# 4. Outside of the class => object reference,classname

# How to modify static variable:
# 1. within the class we should use classname,cls variable
# 2. Outside of the class => only classname

# How to delete Static Variable:
# With in the class we should use classname, clsvariable

class staticvariableClass:
    # Static variable or class level variable
    pi=3.14              # Declaration of Static variable
    cName='IIT'          # Declaration of Static variable
    l = 10               # Declaration of Static variable
    m = 100  # Declaration of Static variable
    #constructor with instance variable for initialization
    #
    def __init__(self,solarsys,country,city,name,rollno):
        # del staticvariableClass.l   # Deletion of Static variable inside constructor [this is valid]
        self.solarsys=solarsys
        self.country=country
        self.city=city
        self.name=name
        self.rollno=rollno
        # Static variable or class level variable in constructor
        staticvariableClass.Company="XYZ"  # Declaration of Static variable
        staticvariableClass.b=20     # Declaration of Static variable


    #instance method
    def methodName(self):
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

    @classmethod
    def m2(cls):
        cls.d=40
        staticvariableClass.e=50
        del cls.m           # Deletion of Static variable inside class method

    @staticmethod
    def m3():
        staticvariableClass.f=60
        del staticvariableClass.f   # Deletion of Static variable inside static method

    def m1(self):
        staticvariableClass.c=30
        print(self.cName)       # Accessing of Static variable
        # del staticvariableClass.cName

    def area(self,r):
        if (r > 0):
            return staticvariableClass.pi * r * r # using of Static variable
# Function creation
def fact(num):
    #factorial=0
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)
    #return fact(num)
    #    print('Factorial of number is:',)

staticvariableClass.g=70

print(staticvariableClass.__dict__)
del staticvariableClass.g # Deletion of Static variable outside class
print(staticvariableClass.__dict__)

objSolar=staticvariableClass('Venus','UK','London','Akash','101')
objSolar1=staticvariableClass('Mars','USA','New York','Akash Gupta','102')
objSolar.m1()
print(staticvariableClass.__dict__)
objSolar.methodName()
print(staticvariableClass.__dict__)
print(fact(5))
print(objSolar.fact(5))
print(staticvariableClass.__dict__)
print('Print instance & static variable :')
print(objSolar.name,objSolar.rollno,objSolar.solarsys,objSolar.country,objSolar.city,staticvariableClass.cName)
# print(staticvariableClass.__dict__)
# print('Print instance & static variable :')
# print('Instance variable value changed with Objects but Static variable keeps same value across all objects:')
# print(objSolar1.name,objSolar1.rollno,objSolar1.solarsys,objSolar1.country,objSolar1.city,staticvariableClass.cName)
# print(staticvariableClass.__dict__)
# print("The area of circle is = ",objSolar.area(99.5))
# print(staticvariableClass.__dict__)
# print("The area of circle is = ",objSolar.area(919.5))
#instanceClass.fibonacci(5)