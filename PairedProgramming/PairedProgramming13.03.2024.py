'''
Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
•
• Note: The bus seating capacity is 50 so the final fare amount should be 5500. 
You need to override the fare() method of a Vehicle class in Bus class.
'''

class Vehicle():
    def __init__(self,capacity):
        self.capacity = capacity
        
    def fare(self):
        total_fare = self.capacity * 100
        return total_fare     

class Bus(Vehicle):
    def __init__(self,capacity=50):
        super().__init__(capacity)
    
    def fare(self):
        total_fare = super().fare() + 0.1 * super().fare()
        return int(total_fare)

bus = Bus()
print(f"The total fare is ${bus.fare()}")