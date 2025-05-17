# Using Self
# Assignment:Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor.
# Add a method display() that prints student details.


class StudentsDetail: # class naming convention should be PascalNaming convention.
# now create constructor otherwise python will create contructor by default,
    def __init__(self, name, marks): # this is constructor(__init__).

# self is a reference parameter to refer every parameter and its syntax is self.name.
# self parameter is for helping to call attributes(properties).
# self parameter mandatory to pass in every method(function).

        self.student_name = name    # it is instance variable.
        self.student_marks = marks  # it is instance variable.
# after = name and marks are the parameter.

# now we are generating a method to print students details.

    def display(self):
        print(f"Name: {self.student_name}  Student Marks: {self.student_marks}")

# now we are creating a variable to pass class in it.
s1 = StudentsDetail("Faizan", 99) # this is Object.

# now we can access class by its variable with dot notation for displaying student data. 
s1.display()
# self parameter call itself due to call instance variable.


