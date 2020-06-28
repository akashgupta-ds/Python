# ----------- Inner Class -------------
# The class which is defined inside another class is called Inner Class.
# Without existing of one type of objects ,If there is no chance of existing of another type of objects then we should go for Inner Class.
# Inner class object is always associated with outer class object.
# Readability of classes improved
# Better performance / memory management.

class Outer:
    def __init__(self):
        print('Outer class object creation')

    def OuterInstanceMethod(self):
        print('Outer class instance method')

    class Inner:
        def __init__(self):
            print('Inner class object creation')
        def InnerInstanceMethod(self):
            print('Inner class instance method')

oObj=Outer()            # inner class object
innerObj=oObj.Inner()   # outer class object
innerObj.InnerInstanceMethod()
innerObj=Outer().Inner()
oObj.OuterInstanceMethod()

