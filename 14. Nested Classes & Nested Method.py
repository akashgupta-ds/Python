#---- Nested Class & Nested Methods ---------------
# Same as inner class
# The class which is defined inside another class is called Inner Class.
# Without existing of one type of objects ,If there is no chance of existing of another type of objects then we should go for Inner Class.
# Inner class object is always associated with outer class object.
# Readability of classes improved
# Better performance / memory management.
#---- Nested Methods ------------------------------
# Inside method declare one or more methods is called Nested Method
# If we want to repeat the methods property, or functionality , we use nested method.
# Code reusability
#************
# is it possible to pass the function as argument ?
# Yes e.g. filter,map,reduce
# Similarly a function can return other function
# while return no parenthesis is required



class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dob=self.DOB(dd,mm,yyyy) # creating object of inner/nested class

    def display(self):
        print('Name of the Person is :',self.name)
        self.dob.display()             # calling method of inner/nested class

    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print('Date of Birth {}/{}/{}'.format(self.dd,self.mm,self.yyyy))
            # Nested method
            def sum(a,b):
                print('First Arguement :', a)
                print('Second Arguement :', b)
                print('The Sum is :', a+b)
            # Nested method call in parent method
            sum(10,20)
            sum(10000,878992)


p=Person('Sunny',24,6,2020)
p.display()
p.dob.display()


# A function can return another function

def outer():
    print('Outer function started')
    def inner():
        print('Inner function execution')

    print('Outer function returning inner function')
    return inner                                # A function can return another function
f1=outer()      # outer & inner function call
f1()
f1=outer        # for outer function we are giving another name /function aliasing

#return inner                                # A function can return another function
#return inner()                              # This returns function output
