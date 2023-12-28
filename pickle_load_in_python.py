# pickle_load_in_python.py

import pickle
from pickle_dump_in_python import Food

with open('cheese.dat','rb') as file:
    cheese = pickle.load(file)

print(cheese.carbs)
print(cheese.calc_calories())


with open('pantry.dat','rb') as file:
    Pantry = pickle.load(file)

egg = Pantry['egg']
print(egg.calc_calories())