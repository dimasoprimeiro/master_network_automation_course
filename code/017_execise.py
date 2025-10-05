"""

Challenge #1

Consider this text file that contains multiple duplicate MAC addresses.

Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.


"""

with open('macs.txt') as f:
    content = f.read().split()

    content = list(set(content))
    print(content)

with open('mac_unique.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')