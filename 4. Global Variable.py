# Global Variable
# From the class we can access global varaibles directly
# Within the method of a class we can declare global variable by global Keywords
# To make a local variable as global variable. It changes the global variable value from local variable.
# to declare global variable explicitly in function (directly)
# global a #valid in function locally
# global a=10 #invalid syntax

class globalVarClass():
    global pi               # making a global variable
    pi=3.14
    a=10
    def __init__(self,r,h):
        self.r=r
        self.h=h

    def cylinderVolume(self):
        #pi=4
        #print(pi)
        print("Cylinder Volume is :",pi * self.r * self.r * self.h)

    def f1(self):
        global a            # making 'a' as global variable
        a=20
        print('After making Global Variable : ',a)

    def f2(self):
        print('Printing ''a'' Variable : ',a)      #changed local variable a.




objGlobal=globalVarClass(3,4)
objGlobal.cylinderVolume()


objGlobal.f1()
objGlobal.f2()
