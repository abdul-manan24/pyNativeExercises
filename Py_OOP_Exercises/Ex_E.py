# __Challenge__

# Define a class attribute”color” with a default value
# white. I.e., Every Vehicle should be white.

class Vehicle:

    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_volvo = Bus("School volvo", 240, 18)
audi_Q5 = Car("Audi Q5", 240, 18)

print(f"Name: {school_volvo.name}, Color: {school_volvo.color}")
print(f"Name: {audi_Q5.name}, Color: {audi_Q5.color}")

# __Expected Output__

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18