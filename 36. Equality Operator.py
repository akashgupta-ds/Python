# ---------------Equality Operator --------------
# == , !=
# == : if contents are same then True else False
# chaining operator works here
# with operations we can also check
# Equality operator never raise an error while comparison
# '=' is assignment operator
# '==' is comparison operator
# 'is' helps to compare address
# '==' helps to compare content
#  Case Sensitivity

print(10==20)  # False : if contents are same then True else False
print(10!=20)  # True : if contents are same then True else False
print(10==True)# False : if contents are same then True else False
print('durga'=='durga')# True : if contents are same then True else False
print(10=='durga')# False : if contents are same then True else False

# chaining operator works here
print(10==20==30==40==50=='durga')# False : if contents are same then True else False

# with operations we can also check
print(10+20==30==10*3)# False : if contents are same then True else False

# Equality operator never raise an error while comparison
print(10==10.0)     # True
print(10=='10')     # False
print(1==True)      # True
print('akash'=='Akash') #False  Case Sensitivity

# is Operator
l1=['A','B','C']
l2=['A','B','C']
print(id(l1))
print(id(l2))
print(l1 is l2 )        # false address comparison
print(l1 == l2 )        # true content comparison
l3=l2
print(l3 is l2)