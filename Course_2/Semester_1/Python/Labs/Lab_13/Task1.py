from datetime import datetime

class Bus:
    def __init__(self, driver_name, bus_number, route_number, brand, start_year, kilometrage):
        self.driver_name = driver_name
        self.bus_number = bus_number
        self.route_number = route_number
        self.brand = brand
        self.start_year = start_year
        self.kilometrage = kilometrage

    def __str__(self):
        return f"Driver name: {self.driver_name}\nBus number: {self.bus_number}\nRoute number: {self.route_number}\nBrand: {self.brand}\nStart year: {self.start_year}\nKilometrage: {self.kilometrage}\n"

    def set_driver_name(self, data):
        self.driver_name = data

    def get_driver_name(self):
        return self.driver_name
    
    def set_bus_number(self, data):
        self.bus_number = data

    def get_bus_number(self):
        return self.bus_number
        
    def set_route_number(self, data):
        self.route_number = data

    def get_route_number(self):
        return self.route_number
    
    def set_brand(self, data):
        self.brand = data

    def get_brand(self):
        return self.brand
    
    def set_start_year(self, data):
        self.start_year = data

    def get_start_year(self):
        return self.start_year
    
    def set_kilometrage(self, data):
        self.kilometrage = data

    def get_kilometrage(self):
        return self.kilometrage

    def years_in_operation(self):
        current_year = datetime.now().year
        return current_year - self.start_year
    
buses = [
    Bus("Homer J Simpson", "AA1234", 101, "Mercedes", 2017, 50000),
    Bus("Johny Depp", "BC5678", 102, "Volvo", 2015, 80000),
    Bus("Bart White", "DE9012", 103, "MAN", 2019, 30000),
]

def find_buses_by_route(buses, route_number):
    return [bus for bus in buses if bus.route_number == route_number]

def find_buses_by_years(buses, years):
    return [bus for bus in buses if bus.years_in_operation() > years]

def find_buses_by_kilometrage(buses, kilometrage):
    return [bus for bus in buses if bus.kilometrage > kilometrage]


route_criteria = 103
print(f"Buses by route {route_criteria}: \n")
for bus in find_buses_by_route(buses, route_criteria):
    print(bus.__str__())

years_criteria = 5 
print(f"Buses by {years_criteria} years in operation: \n")
for bus in find_buses_by_years(buses, years_criteria):
    print(bus.__str__())

kilometrage_criteria = 60000 
print(f"Buses by {kilometrage_criteria} km of kilometrage: \n")
for bus in find_buses_by_kilometrage(buses, kilometrage_criteria):
    print(bus.__str__())