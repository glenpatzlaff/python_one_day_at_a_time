class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} with a {self.battery_size}-kWh battery."

my_electric_car = ElectricCar("Tesla", "Model S", 2019, 75)
print(my_electric_car.display_info())

