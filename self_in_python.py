# self_in_python.py
# what is self in python?
# self is a struct variable in class
# Under the same class, self can pass through other def methods
# the parameter self in a class stores in the same memory

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name} and level {self.level}.")
        # parameter: self: self@player
    def play(self):
        self.level += 1


#
player1 = Player("Harry", 100)
player2 = Player("Tamin", 200)
player3 = Player("Kiki", 300)

player1.introduce()
player1.play()
print('level: ', player1.level)
player1.introduce()