# seek_tell_in_python.py
# seek and tell: file handling

file = open("./pyLearnYoutube/sample.txt", "r")
position = file.tell()
print("Current position:", position)

file.seek(10,0)
position = file.tell()
print("Current position:", position)