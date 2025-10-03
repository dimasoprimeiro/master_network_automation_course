import csv

with open('devices.txt', 'r') as devices_file:
    leitor = csv.reader(devices_file, delimiter=':')

    for coluna in leitor:
        print(coluna)



