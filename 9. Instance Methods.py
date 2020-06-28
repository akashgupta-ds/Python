# Instance Method
# Inside method body if we are using atleast one instance variable then that method, we should declare as instance method
# To declare instance method we are not required to use any decorator
# The first argument to the instance method should be self,which is reference to current object,
# We can access instance variable inside method.
# Inside instance method we can access both instance variable and static variable.
# We can call instance method by using object reference.

# Instance method with Linear Regression ex
#Y – Dependent Variable
#a – Slope
#X – Independent variable
#b – Intercept
#Y=a*X + b

# class for lienar regression
class clsLinearRegression:
    # declaration of coefficients,global variable
    global X
    X=0.3
    #constructor
    def __init__(self,a,b):
        self.a=a
      #  self.X=X
        self.b=b
    # instance method
    def calculation(self):

        for i in range(0,10):
            y= self.a * X + self.b
            print("The values for X is {} & Y axis is {} :".format(X,  y))
            self.a=self.a * 4
            self.b=self.b * 7.6


    # user input

obj=clsLinearRegression(11.5,13.6)
obj.calculation()
