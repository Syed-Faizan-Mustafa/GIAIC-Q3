# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

# MRO is the order in which the methods are called.
# Diamond Inheritance is a type of inheritance where a class inherits from two or more classes.
# MRO check from left to right.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

d = D()
print(D.__mro__)    
print(d.show())
        
        
