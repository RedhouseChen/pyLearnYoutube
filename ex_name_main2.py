# ex_name_main2.py
# __name__: built-in variable in python. It represents the current module's name
# if __name__ == '__main__': A way to ensure that a specific block of code runs only when the Python script is executed directly
# Not when it's imported as a module.

from ex_name_main import greet

name = "John Doe"
result = greet(name)
print(f"Hi, {result}.")
print(f"__name__ is {__name__}")