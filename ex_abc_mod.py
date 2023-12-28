# ex_abc_mod.py
# Abstract Base Class
from abc import ABC

class Fruit(ABC):

    @abstractmethod
    def have_seed(self):
        pass

    @abstractmethod
    def color(self):
        pass

class Apple(Fruit): # Inherited from ABC
    def __init__(self):
        self.seed = True
        self.color = "Red"

    def have_seed(self): # Implemented ABC Method
        return self.seed()
    
    def color(self): # Implemented ABC Method
        return self.color()
    
# 
my_apple = Apple()
print(my_apple)