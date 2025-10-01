# f = open('configuration.txt')
# content = f.read(5) #read 5 caracters after the cursor
# print(content)

# content = f.read(3)#read 3 caracters after the cursor
# print(content)

# print(f.tell()) #show where the cursor is

# f.seek(2)
# content = f.read(3)#read 3 caracters after the cursor
# print(content)

# f.seek(0)
# content = f.read(3)#read 3 caracters after the cursor
# print(content)

f = open('configuration.txt')
print(f.read())
#do stuff
print('#' * 50)
f.seek(0)
print(f.read())


