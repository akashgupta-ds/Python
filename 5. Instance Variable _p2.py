# Where we can declare instance variable
# 1. Inside constructor by using self
# 2. Inside instance method by using self
# 3. From outside of the class by using object reference.

# How to access instance Variable:
# 1. within the class by using self
# 2. outside of the class by using object reference

# How to delete instance variable:
# 1. del self.variablename -----INSIDE CLASS
# 2. del objectreference.variablename -------OUTSIDE CLASS

class Student:
    def __init__(self,name,rollno):
        # Instance variable initialization
        self.name=name
        self.rollno=rollno
    # Instance method
    def info(self):
        # instance variable
        self.marks=99
        print('Student Name is :', self.name)
        print('Student Rollno is :', self.rollno)
        print('Student Marks is :', self.marks)
        x=10 # local variable

    def m1(self):
        self.e=50

    # delete instance variable
    def delete(self):
        del self.name

s1=Student('Akash',101)
print(s1.__dict__) # Till this point only 2 instance variable created
s1.info()
print(s1.__dict__) # Till this point only 3 instance variable created
s1.age=33 # if already exists then replace otherwise create new instance variable
print(s1.__dict__) # Till this point only 4 instance variable created
t2=s1.m1()
print(s1.__dict__) # Till this point only 5 instance variable created
# deletion of object --name will be deleted as declared in function
s1.delete()
print(s1.__dict__) # Till this point only 4 instance variable created
del s1.rollno
print(s1.__dict__) # Till this point only 3 instance variable created
