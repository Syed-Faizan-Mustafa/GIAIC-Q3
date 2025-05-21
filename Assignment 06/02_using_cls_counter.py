# Using cls
# Assignment:Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

# we are having 3 types of variable in python OOP
# 1 - Instance Variable.
# 2 - Class Variable.
# 3 - Local Variable.

# in lesson 01 we created instance variable now we are creating and understanding class variables.

# variable created with in the class it is called class variable.
class Counter:
    count = 0   # it is class variable. which is method of class.

# Now creating a constructor as per rule good python programmer rules and pass the self parameter in it.
    def __init__(self):
        Counter.count += 1 # its counter object, this function will work: how many objects we have created?
# Now we are using python pre defined Decorator. Decorator name always starts with @ sign.
    @classmethod # to print(this decorator is working for printing or displaying)
# ab jitna bhi code main likhonga decorator main woh classmethod decorator ka hojayega.
# classmethod decorator is uses for helping to access class variables.
    def show_count(cls):
        print(f"Total Objects Created: {cls.count}") # cls hum class method k variable ko access karne k liye use kartay hain.
        # Unlike self (which refers to an instance), cls allows you to modify or access class-level data.
# agar hum yahan class method ka use nahi karengay tuo hamaray paas ek specific error ayega due to not using class method.
# is liye hum class ka istamaal kar rahay hain, hum direct access nahi kar saktay class variable ko, isliye humne classmethod ka use kia.

# Now we are going to create objects.
Object1 = Counter() # it is object.
Object2 = Counter() # it is object.
Object3 = Counter() # it is object.
Object4 = Counter() # it is object.

Counter.show_count()

# What is the purpose of cls.
# cls refers to the class Student.
# change_school() updates the class variable school_name.
# Unlike self (which refers to an instance), cls allows you to modify or access class-level data.

#        Difference between self and cls
# Keyword	        Refers To	        Used In
# self	         Object/Instance    Instance Methods
# cls	          Class itself	     Class Methods

