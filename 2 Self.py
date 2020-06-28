#---------------- self ------------------------------------
# this keyword in JAVA is equivalent to self in PYTHON
# self variable always pointing to current object and also implicit variable
# within the python class to refer the current object we should use self variable
# self is always pointing to Employee class object
# The first argument to the constructor and instance method must be 'self' e.g. info(self)
# PVM is responsible to provide value for self argument and we are not required to provide explicitly
# By using self we can declare instance variable
# By using self we can access instance variable
# No type error while accessing instance variable in self
# as the order it will assign the values
# Pass by keyword if the order is not same
# IMP: FIRST NAME in the CONSTRUCTOR will be treated as 'self' internally
# def __init__(s):
#   s.name=name         # valid self replaced with s




class Employee:
    '''Class to understand the use of self variable'''
    # Constructor
    def __init__(self,eno,ename,esal,eaddr):
    # INSTANCE VARIABLE DECLARATION & INTIALIZATION
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    # PROOF: within the python class to refer the current object we should use self variable
    # The id of self and class object is same
        print('Self ID:',id(self))

    # INSTANCE METHOD DECLARATION
    def info(self):
        # The method where we use instance variable using self
        print('Employee No. :',self.eno)
        print('Employee Name. :', self.ename)
        print('Employee Salary. :', self.esal)
        print('Employee Address. :', self.eaddr)

e1=Employee(100,'Akash',1000000,'Delhi')
e2=Employee(101,'Akash Gupta',1000000,'London')
e1.info()
e2.info()
# PROOF: within the python class to refer the current object we should use self variable
print('Object-1 ID:',id(e1))
print('Object-2 ID:',id(e2))
#   How to print doc string in our class
#   Document String:
#print(Employee.__doc__)
#   To check all the methods and objects of a class
#help(Employee)

