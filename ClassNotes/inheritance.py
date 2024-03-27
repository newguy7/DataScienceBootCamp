class Vehicle():
    def __init__(self):
        print("This is a vehicle")        

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("This is a car.")

class CityRide(Car):
    def __init__(self):
        super().__init__()
        print(f"This is a CityRide Car")
        
class OffRoad(Car):
    def __init__(self):
        super().__init__()
        print(f"This is a OffRoad Car")

class SUV(CityRide,OffRoad):
    def __init__(self,type="SUV"):
        super().__init__()

cityride1 = CityRide()
offroad1 = OffRoad()
suv1 = SUV()