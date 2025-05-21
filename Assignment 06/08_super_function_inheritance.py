# 8. The super() Function
# Assignment:Create a class Person with a constructor that sets the name. Inherit a class Teacher from it,
# add a subject field, and use super() to call the base class constructor.

# Base/Parent class / Person is a base (parent/super) class
class Person:
    def __init__(self, name): # constructor 
        self.personName = name #It has an __init__() method that sets an instance variable personName.

# Sub/Child Class
class Teacher(Person): # Teacher is a child inherit from Person. 
    def __init__(self, name, subject): # it also has its own constructor(__init__).
        # super().__init__(name) calls the parent class's constructor to initialize personName.
        super().__init__(name) # inherit parent class's method and using parent name which is in the Person parameter.
        self.mySubject = subject #Then, mySubject is added as a new instance variable specific to Teacher.

teacher = Teacher("Faizan Mustafa", "IT")
print(teacher.personName)
print(teacher.mySubject)

# 🧠 Concepts Demonstrated:
# Concept	                    Description
# Class	                    Blueprint for objects
# Inheritance	            Teacher inherits from Person
# super()	                Calls the parent class's method
# Instance Variables	    personName and mySubject are unique per object
