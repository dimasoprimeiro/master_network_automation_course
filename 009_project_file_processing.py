# PROJECT: FILE PROCESSING

with open('device.txt') as f:
    content = f.read().splitlines() # joga o conteúdo do arquivo na lista
    # print(content)
    devices = list() #torna devices em uma lista vazia
    for line in content[1:]:
        devices.append(line.split(':'))
    print(devices)

    for device in devices:
        print(f'pinging {device[1]}')


