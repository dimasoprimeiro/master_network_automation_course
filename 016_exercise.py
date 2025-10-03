import csv 

with open('devices.txt', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=':')
    my_list = list()


    for row in reader:
        my_list.append(row)

print(my_list)
    
    