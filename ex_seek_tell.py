# ex_seek_tell.py
# seek and tell: file handling

file = open("./sample.txt", "r")
position = file.tell()
print("Current position:", position)

file.seek(10,0)
position = file.tell()
print("Current position:", position)