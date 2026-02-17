# __Challenge__

# Check object is a subclass of a particular class.

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

# Write a code to check the following.

# Dog is a subclass of Animal? –> True
print(f'Dog is a subclass of animmal: {issubclass(Dog, Animal)}')
# Animal is a subclass of Dog? –> False
print(f'Animal is a subclass of Dog? {issubclass(Animal, Dog)}')
# Cat is a subclass of Animal? –> False
print(f'Cat is a subclass of Animal? {issubclass(Cat, Animal)}')
# Puppy is a subclass of Animal? –> True
print(f'Puppy is a subclass of Animal? {issubclass(Puppy, Animal)}')