# 13. Composition 
# # composition means ek class dosri class k object ko apne andar rakhaygi matlab ek cheez dosri cheez ka hissa hai 
# isay composion kehtay hain.
# Assignment: Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class 
# during initialization. Access a method of the Engine class via the Car class.

# ek class k method ko dosri class main call karwana hai.

class Engine:
    def start(self):
        print("Engine Started Now you can drive")

class Car:
    def __init__ (self, engine):
        self.carEngine = engine

    def engine_start(self):
        self.carEngine.start()

e = Engine()
c = Car(e)      # this is aggregation also.
c.engine_start()