# ex_getitem.py

class MyList:
    def __init__(self):
        self.data = [1, 2, 3]
    
    def __getitem__(self, index):
        return self.data[index]


# 

my_list = [1, 2, 3]
print(my_list[0])

custom_list = MyList()
print(custom_list[1])
