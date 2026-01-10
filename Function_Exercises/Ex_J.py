# __Challenge__

# Define a function describe_pet(animal_type, pet_name)
# that prints a description of a pet. Call this function
# using both positional and keyword arguments.

def describe_pet(animal_type, pet_name):
    print(f"animal_type: {animal_type}---pet_name: {pet_name}")

describe_pet("Dog", "Tom")
describe_pet(pet_name="Jerry", animal_type="Mouse")