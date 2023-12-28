# ex_map_func.py
# Map Function: map(function, iterable)
#                - Returns an iterator that applies function to every item of iterable.

def make_even(num):
    if num%2 == 1:
        return num+1
    else:
        return num
    
x = [441, 521, 235, 122, 432, 346]

y = []
for num in x:
    y.append(make_even(num))

print(y)

# map
z = map(make_even, x)
print(list(z))