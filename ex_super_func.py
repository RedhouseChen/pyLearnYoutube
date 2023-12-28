# ex_super_func.py
# super(): Code Reusability and Code Maintainability

# parent class
class Animal:
    def speak(self):
        print("Animal souund")

# subclass
class Dog(Animal):
    def speak(self):
        super().speak() # Call the 'speak' method of the parent class
        print("Woof!")

#
dog_instance = Dog()
dog_instance.speak()