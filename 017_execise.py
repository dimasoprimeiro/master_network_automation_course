with open('macs.txt') as f:
    content = f.read().split()

    content = list(set(content))
    print(content)

with open('mac_unique.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')