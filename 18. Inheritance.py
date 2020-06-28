# ------------- Inheritance ------------------
# Code reusability
# By this existing functionality we can extend.
# Inheritance Types :
# 1. Single Inheritance         # A => B
# 2. Multilevel Inheritance     # A => B => C
# 3. Hierarchical Inheritance   # P=> C1,C2,C3
# 4. Multiple Inheritance       # A,B=> C
# 5. Cyclic Inheritance         # A <=> B
# 6. Hybrid Inheritance         # Single + Multiple + Multilevel+ Hierarchical



class P:
    def property(self):
        print('Ghar+Gadi+Bangla')

    def marry(self):
        print('Subbalaxmi')

# Inheriting the methods & properties of parent class with child class
class C(P):
    def family(self):
        print('family is first')
    def marry(self):
        print('With a girl')
        super().marry()  # calling parent method

c=C()
c.property()
c.marry() # showing the child & parent methods properties