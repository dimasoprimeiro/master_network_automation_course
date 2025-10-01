f = open('configuration.txt', 'rt')
content = f.read()
print(content)
print(f.closed)
f.close