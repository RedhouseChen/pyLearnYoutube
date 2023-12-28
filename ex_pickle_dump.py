# ex_pickle_dump.py

import pickle

class Food():
    def __init__(self):
        self.protein = 0
        self.carbs = 0
        self.fat =0

    def calc_calories(self):
        calories = self.protein*4 + self.carbs*4 + self.fat*9
        return calories
    
#
Pantry = {}    

cheese = Food()
print(cheese.protein)

cheese.protein = 9
cheese.carbs = 1
cheese.fat = 9
Pantry['cheese'] = cheese

egg = Food()
egg.protein = 5
egg.carbs = 1
egg.fat = 4
Pantry['egg'] = egg

with open('cheese.dat','wb') as file:
    pickle.dump(cheese, file)

with open('pantry.dat','wb') as file:
    pickle.dump(Pantry, file)