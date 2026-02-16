# __Challenge__

# Create a child class Bus that will inherit all of the
# variables and methods of the Vehicle class.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

Bus1 = Bus('Yutong', 240, 18)

print(f"Name of bus: {Bus1.name}")
print(f"Speed of bus: {Bus1.max_speed}")
print(f"Mileage of bus: {Bus1.mileage}")