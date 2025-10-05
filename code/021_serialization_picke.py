#data serialization in Python
import pickle


friends1 = {
    'Dan' : [20, 'Osasco', 978055191],
    'Maria': [25, 'London', 932838972],
}

friends2 = {
    'Kaue' : [23, 'Carapicuiba', 97805335191],
    'Renan Augusto': [25, 'Sydney', 9328333338972],
}

friends = (friends1, friends2)

with open('files/friends.dat', 'wb') as f:#criou o arquivo com as informacoes do dicionario
    pickle.dump(friends, f)

with open('files/friends.dat', 'rb') as f:# abriu o arquvio binario
    obj = pickle.load(f) #colocou o conteudo na variavel
    print(type(obj))
    print(obj)
