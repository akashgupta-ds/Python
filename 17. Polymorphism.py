# ------------ Polymorphism -----------------
# Polymorphism :- One Name many form
# Polymorphism can be acheived through two ways:-
# 1. Overloading : [Operator , Method , Constructor]
# *****Python does not support Method & Constructor overloading
# *Two methods are said to be overloaded if the name are same but different argument types.
# ***But in python we don't have types to specify explicitly
# ****In python if we do method overloading then the last method will be considered.
# **Python does not support method/constructor overloading because the python supports dynamic data type,so there
# is no need to have the overload
# Variable length arguments
# Use fixed length arguments
# 2. Overriding :[Method, Constructor]

class Book:
    def __init__(self,pages):
        self.pages=pages
    # Magic method related to operator
    def __add__(self, other):
        return  self.pages + other.pages
    def __sub__(self, other):
        return self.pages-other.pages
    def __mul__(self, other):
        return self.pages*other.pages

b1=Book(100)
b2=Book(200)
# whenever we are calling + operator the __add__() method will be called
# whenever we are printing any object reference / object then __str__() will be called. If we are not providing this
# method then default implementation will be executed.
print(b1+b2)
b3=Book(700)
#print(b1+b2+b3) #Invalid
print(b2+b3)
print(b2-b1)
print(b2*b1)

# Default arguements
# variable length arguments
class Test:
  # fix length arguments
  #  def sum(self,a=None,b=None,c=None):
  #      if(a!=None and b!=None and c!=None):
  #          print('The sum of 3 no.:',(a+b+c))
  #      elif (a != None and b != None ):
  #          print('The sum of 2 no.:', (a + b))
  #      else:
  #          print('Please provide 2 Or 3 args')
    def sum(self,*a):  # variable length arguments
        total=0
        for x in a:
            total=total+x
            print('The sum is :',total)
t=Test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)

