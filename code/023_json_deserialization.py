import json

with open('files/friends.json', 'rt') as f: #carregou de um arquivo .json
    obj = json.load(f)
    print(type(obj))
    print(obj)

json_string = """{
    "Dan": [
        20,
        "London",
        3234342
    ],
    "Maria": [
        25,
        "Madrid",
        43525222
    ]
}"""

obj = json.loads(json_string) #carregou de um string

print(type(obj))
print(obj)