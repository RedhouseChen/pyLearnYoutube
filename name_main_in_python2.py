# name_main_in_python2.py
# __name__: built-in variable in python. It represents the current module's name
# if __name__ == '__main__': A way to ensure that a specific block of code runs only when the Python script is executed directly
# Not when it's imported as a module.

from name_main_in_python import greet

name = "John Doe"
result = greet(name)
print(f"Hi, {result}.")