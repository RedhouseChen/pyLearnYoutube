# ex_init_method.py
# initializer: initialize parameter, variable

#class MyClass:
#    def __init__(self, arg1, arg2, *args, **kwargs):
#        # Initialization code here

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the Dog class
my_dog = Dog('Buddy', 3)
print(my_dog.name)
print(my_dog.age)