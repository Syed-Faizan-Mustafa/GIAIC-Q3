# Public Variables and Methods
# Assignment:Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.carType = brand

    def car_start(self):
        print(f"My {self.carType} Car is starting.")

car = Car("Toyota")
print(car.carType)
car.car_start()
