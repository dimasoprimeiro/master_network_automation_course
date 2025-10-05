with open('devices.txt', 'r') as f:
    devices = f.read(). splitlines()
    # print(devices)

minha_lista = list()
for i in devices:
    tmp = i.split(':')
    minha_lista.append(tmp)

print(minha_lista)

# print(minha_lista[0][2])