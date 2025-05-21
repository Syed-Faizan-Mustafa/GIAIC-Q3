# 5. Static Variables and Static Methods
# Assignment:Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be
# used.

class MathUtils:
    @staticmethod # na hum yahan class variable use karne walay hain na instance variable use karne walay hain
    # jo bhi function banay hain class main, hum usay method kehtay hain or method ko call hum parentheses k saath kartay hain.
    # static method ka faida hota hai k aap yahan koi reference parameter nahi dete or static method ko withour object call karsaktay hain.
    # static method helper function kehlatay hain oop main utility/ helper function kehlatay hain inside the clas.
    # So in your case, since add(a, b) just takes two arguments and returns a result without using any class or object data,
    # it is rightly a @staticmethod.

    # Called using class or object:
    def add(a , b):
        return a+b
    
print(MathUtils.add(0,10))

# 🧠 Instantiation in simple terms:
# Instantiation = Calling the class like a function to create an object.

# Behind the scenes:
# s1 = Student(Ali,20)

# Calls __new__() → allocates memory.
# Calls __init__() → initializes object.
# Returns a new instance of Student.