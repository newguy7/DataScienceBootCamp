'''
Create a Python class called Car that represents a basic car. 
The Car class should have the following properties and methods:
Properties:
make: A string representing the make of the car (e.g., "Toyota", "Ford").
model: A string representing the model of the car (e.g., "Camry", "F-150").
year: An integer representing the year the car was manufactured.
odometer_reading: An integer representing the current odometer reading of the car.
Methods:
get_description(): A method that returns a formatted string describing the car, including its make, model, and year.
read_odometer(): A method that prints the car's mileage.
Ensure that the odometer_reading property is private and can only be modified through a method named update_odometer(). 
This method should take in a new odometer reading and update the odometer_reading property only 
if the new reading is greater than the current reading.

'''

class Car():

    def __init__(self, make:str, model:str, year:int, odometer_reading:int):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = odometer_reading

    def get_description(self):
        return f"{self.make} {self.model} {self.year}"
    
    def read_odometer(self):
        print(f"Total distance travelled: {self.__odometer_reading}")

    # setter
    def update_odometer(self,new_odometer_reading):        
        if new_odometer_reading > self.__odometer_reading:
            self.__odometer_reading = new_odometer_reading

car1 = Car("Toyota","Camry",2024,500)
car2 = Car("Honda","Accord",2023,3000)

# get the description of the car

car1_detail = car1.get_description()     
print(car1_detail)

car2_detail = car2.get_description()   
print(car2_detail)

# read the car mileage
car1_mileage = car1.read_odometer()

car2_mileage = car2.read_odometer()

# update the odometer reading
car1_updated_mileage = car1.update_odometer(300)
car1_mileage = car1.read_odometer()

car2_updated_mileage = car2.update_odometer(3400)
car2_mileage = car2.read_odometer()

