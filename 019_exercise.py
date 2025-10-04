"""
Challenge #2

Create a Python script that reads a text file into a list and then converts the list into a string that has the entire file content.

"""

with open('sample_file.txt', 'r') as f:
    content = f.read().splitlines() #transformando o arquivo em uma lista
    my_str = '\n'.join(content) # retornando o arquvio para str
    print(my_str, type(my_str))






