# Danny Radosevich
# COSC1101
# Classes

class Car:
    def __init__(self, make , model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_od(self):
        print(f"{self.odometer_reading}")

    def update_od(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage

    def increment_od(self, miles):
        if miles >= 0:
            self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def get_battery(self):
        return self.battery_size
    

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        print(f"This car has a {self.battery.get_battery()} kWh battery")

#base car class
new_car = Car("audi", "a4", 2019)
print(new_car.get_descriptive_name())

new_car.odometer_reading = 23 
new_car.read_od()

#electric car class 
volt = ElectricCar("Chevy", "Volt", "2020")
print (volt.get_descriptive_name())