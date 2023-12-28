# ex_name_main.py
# __name__: built-in variable in python. It represents the current module's name
# if __name__ == '__main__': A way to ensure that a specific block of code runs only when the Python script is executed directly
# Not when it's imported as a module.

def greet(name):
    print(f"Hello, {name}!")
    return __name__
#
if __name__ == '__main__':
    user_name = input("Enter your name:")
    greet(user_name)
    print(f"__name__ is {__name__}")


