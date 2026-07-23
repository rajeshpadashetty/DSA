class car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =0
    
    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        return f"this car has {self.odometer_reading}miles on it"
    
    def update_odometer(self, mileage):
        if mileage>=self.odometer_reading:\
           
            self.odometer_reading = mileage

        else:
            print("you can't roll back an odometer")

        def increment_odometer(self, miles):
            self.odometer_reading += miles

class electric_car(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


tata=car("tata","nexon",2023)
print(tata.get_car_info())



     
    