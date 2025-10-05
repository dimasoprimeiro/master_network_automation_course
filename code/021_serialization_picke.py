#data serialization in Python

friends = {
    'Dan' : [20, 'Osasco', 978055191],
    'Maria': [25, 'London', 932838972],
}

with open('friends.txt,', 'w') as f:
    f.write(friends)