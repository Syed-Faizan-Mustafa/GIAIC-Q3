# 9. Abstract Classes and Methods
# Assignment:Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

# The ABC module in Python is used for defining abstract base classes, which are a key part of object-oriented programming and
#  help enforce method structure in subclasses.

# 🧠 What Is ABC (Abstract Base Class)?
# An Abstract Base Class is a class that cannot be instantiated on its own. It's used to define methods that must be implemented 
# by any subclass.
# You use the abc module for this, with:
# ABC (base class for abstract classes)
# @abstractmethod decorator (to define required methods)

# ✅ Why use ABC?
# To:
# # Define a common interface for all subclasses.
# Force subclasses to implement specific methods.
# Prevent incomplete base classes from being used.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod 
    def area(self):    # this is the rule of every child class to define this method in its own class.
        pass
# we have lots of angle classes but this method is compulsory to use otherwise it will create issues in programming.
class RectangleShape(Shape):
    def __init__(self, width, height):
        self.rectangleWidth = width
        self.rectangleHeight = height
        
    def area(self):
        return self.rectangleWidth * self.rectangleHeight
    # def areaaaa(self):
    #     return self.rectangleWidth * self.rectangleHeight
    
# creating an object or class instantiate.
rect = RectangleShape(4 ,5)
print(rect.area())

# print(rect.areaaaa())
# but if i change the name of area method like areaaaaa so it will generate an error which will be:
# (TypeError: Can't instantiate abstract class RectangleShape without an implementation for abstract method 'area')
# because we have defined rule k agar humne Jo shape ki class banai hai ye class hamain jahan bhi use karni hai tuo 
# us class k andar jo bhi method define kia hai woh laazmi use hoga otherwise error ajayega.














# 🔍 Summary Table:
# Component	                    Purpose
# ABC	                        Makes a class abstract
# @abstractmethod	            Forces subclasses to implement methods
# No instantiation	            You can't create objects of abstract classes