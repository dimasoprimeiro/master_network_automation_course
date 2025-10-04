"""
Challenge #4

Create a Python function called tail that reads the last n lines of a text file. 
The function has two arguments: the file name and n (the number of lines to read). 
This is similar to the Linux `tail` command.

"""

def tail(file, n):
    with open(file, 'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last n elements of the list
        last = content[len(content)-n:]
        # print(last)
        # concateneting the list back into a string
        my_str = '\n'.join(last)
        return my_str


t = tail('sample_file.txt', 3)
print(t)