# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including 
# the dog's name.

class Dogs:
    def __init__ (self, name, breed):
        self.dogName = name
        self.dogBreed = breed
    
    def bark(self):
        print(f"{self.dogName} sounds woof! ")

sound = Dogs("Tommy", "Bull Dog")
sound.bark()