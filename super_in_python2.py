# super_in_python.py
# super(): Code Reusability and Code Maintainability

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

# subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Call the parent class's constructor
        self.breed = breed

#
my_dog = Dog('Spot', 'Taiwanese')
print(my_dog.name)
print(my_dog.breed)