# It is just general Utility method or helper method
# If we are not using any instance variable inside method body, to define such type of general utility method,we should__
# __go for static methods.
# We can call by using object reference by using class name.
#*** if we are not using any decorator :
#   @staticmethod is optional
#   @classmethod is mandatory
# If we are calling by using object reference then it will be instance method.
# ****And if we are calling by using class name then it should be static method.
# If we are using only static variables then use Static Method.



class Animal:
    # static variable
    legs=4

    def walk(name):     # static method
        # can only access static and class level variables
        print('{} walks with {} legs'.format(name,Animal.legs))



obj=Animal()
#obj.walk('Dog')     #invalid
Animal.walk('Dog')   #valid
Animal.walk('Cat')

## 2ND example

class calcObjects:
    count=0
    def __init__(self):
        calcObjects.count = calcObjects.count + 1

    # static method
    def getNoofObjects(): 
        print('The number of objects created :',calcObjects.count)


obj=calcObjects()
obj1=calcObjects()
obj3=calcObjects()
obj4=calcObjects()



calcObjects.getNoofObjects()