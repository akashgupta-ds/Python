class Student:
    # This is doc string for showing comments and guidance by programmer
    '''This class developed by Akash Gupta'''

    '''Constructor for initializing instance variable'''
    def __init__(self,rollno,name):
        self.name=name
        self.rollno=rollno
        x=10

    '''Instance Method- In this method instance variable can be called with self '''
    def talk(self):
        print('My Name :',self.name)
        print('My Rollno :', self.rollno)


s=Student(100,'Sunny')

''''Python is case sensitive'''
print(s.name)
print(s.rollno)
#print(s.x)
print('Hello Let''s Talk !')

'''Instance method called by reference variable as follows'''
s.talk()

print(Student.__doc__)