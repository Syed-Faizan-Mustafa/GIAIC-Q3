# 12. Static Methods
# Assignment: Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
# we have to use their formula.
# static method kia hote hain:
# jab hum class variable aur instance variable ka use nahi kartay tuo direct static method ka use kartay hain with return
# static method main reference keyword (self,cls) ki zaroorat nahi hoti.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 1.8) + 32
    
print(TemperatureConverter.celsius_to_fahrenheit(10))