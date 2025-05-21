# 6. Constructors and Destructors
# Assignment:Create a class Logger that prints a message when an object is created (constructor) and another message 
# when it is destroyed (destructor).

# Object Constructor to contruct Object:
class Logger:
    def __init__(self):
        print("Object Constructed")

    def __del__(self):
        print("Object Destroyed")

# object instantiate or objects instance or instance of the class/class instance.
# objects instance → ✅ better as "instance of the class" or "class instance"
# basically hamain aisa kehna chahiye k :
# Instance Logger class / create a instance of Logger.
construct = Logger()
# using del keyword to delete Object.
del construct
print(construct) # it will generate an error because it is deleted.
