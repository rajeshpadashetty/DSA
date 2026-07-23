class car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =0
        self.battery_size = 75
    
    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def fill_gas_tank(self):
        return "this car has a gas tank"
    
    
    def read_odometer(self):
        return f"this car has {self.odometer_reading}miles on it"
    
    def update_odometer(self, mileage):
        if mileage>=self.odometer_reading:
           
            self.odometer_reading = mileage

        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):
            self.odometer_reading += miles


    
    def describe_battery(self):
        return f"this car has a {str(self.battery_size)}-kwh battery"
    


class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        return f"this car has a {str(self.battery_size)} BATTERY SIZE" 
    


class electric_car(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

     
    def describe_battery1(self):
        return f"this car has a {str(self.battery.battery_size)}-kwh battery"
    
    def fill_gas_tank(self):
        return "this car does not have a gas tank"
    
    
        
    

tata=car("tata","nexon",2023)
tata1=car("tata","seyara",2025)
tata3=electric_car("tata" ,"seyara",2025)

print(tata.get_car_info())
print(tata1.get_car_info())
print(tata3.describe_battery1())
print(tata.fill_gas_tank())
print(tata1.fill_gas_tank())
print(tata3.fill_gas_tank())

print(tata3.battery.describe_battery())
