# 3. Local Variables
# Method level variables
# we should not use self,cls,classname
# local variable can not be called outside specified block/method
x=100           #Global variable
class localVariableClass():
    a=10
    def __init__(self):
        # del localVariableClass.a  # Deletion of Static variable inside constructor [this is valid]
        print(self.a)
        print(x)

    def degreeMethod(self,radian):
        # local variable
        pi=22/7
        x=999
        degree=radian * (180/pi)
        print("Degree:",degree)
        print("Gloabl Variable changed:", x)

obj=localVariableClass()
# print(obj.__dict__)
obj.degreeMethod(10)
# print(obj.__dict__)
print("Gloabl Variable does not changed:", x)       # Global variable call outside class






print(localVariableClass.a)
print(localVariableClass.__dict__)
objlr=localVariableClass()
print(localVariableClass.__dict__)