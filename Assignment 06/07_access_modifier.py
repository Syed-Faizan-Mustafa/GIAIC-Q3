# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name, a protected variable _salary, 
# and a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

# python protected variable k ziada use ko recommend nahi karti.

class Employee:
    def __init__(self, name, salary, ssn): # __init__ constructor
        # these are the instance variable.
        self.empName = name # public instance variable.
        self._empSalary = salary # it is protected instance becuase we use _sign before the instance variable name.
        self.__ssn = ssn # it is private instance variable becuase we use __ sign (double underscore) before the instance variable.

# objects instance → ✅ better as "instance of the class" or "class instance"
emp = Employee("Faizan", 50000, 433987)
print(emp.empName)
print(emp._empSalary) # protected variable ko is tarha se access karna python ki taraf se recommended nahi hoti.
# print(emp.__ssn) # AttributeError: 'Employee' object has no attribute '__ssn', q k humne isay private banalia hai.

# private variable k liye ek method alag banana parta hai usay access karne k liye, private variable class k variable k bahar
# access nahi karsaktay, lekin agar hum koi method bana k access karna chahain tuo he access kar saktay hain.
# matlab koi dosra method isay access karsakta hai lekin hum is ko class k bahar access nahi karsaktay hain.

# lekin hamain lazmi private ko zabardasti access karna he karna hai tuo us ka tariqa hai:
print(emp._Employee__ssn) # lekin ye tariqa bhi python ki taraf se recommended nahi hai. python q k ek dynamic language hai,
# developer bas ye check karsaktay hain k hamara result show horaha hai k nahi lekin private ko access karne k liye ek method
# banana parta hai jo k private instance variable ko access karta hai class k bahar with the getter method.
