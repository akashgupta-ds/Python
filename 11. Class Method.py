# **Inside method body if we are using only static variable then it is highly recommended to declare that method as class method.
# To declare class method, compulsory we should use @classmethod decorator
# The first arguement to the classmethod should be cls, which is reference variable for current class object and by using that__
# __we can access static variables
# **Inside classmethod we can acces only static variables and we can not access instance variables.
# **We can call class method either by using object reference or by using class name, but recommended to use class name.

class Animal:
    # static variable
    legs=4
    @classmethod
    def walk(cls,name):
        # can only access static and class level variables
        print('{} walks with {} legs'.format(name,cls.legs))

class calcObjects:
    count=0
    def __init__(self):
        calcObjects.count = calcObjects.count + 1

    @classmethod
    def getNoofObjects(cls):
        print('The number of objects created :',cls.count)

obj=calcObjects()
obj1=calcObjects()
obj3=calcObjects()

calcObjects.getNoofObjects()



Animal.walk('Dog')
Animal.walk('Cat')