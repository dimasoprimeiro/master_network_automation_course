#serilizing to a file

def serialize(obj, file, type): #criando a funçao
    if type == 'pickle': # se o tipo for pickle for rodar esse if
        import pickle # importantando o biblioteca pickle
        with open(file, 'wb') as f: # abrindo o arquivo com write binary e colocando na variavel f
            pickle.dump(obj, f) #fazendo o dump na variavel obj , com o recurso f
    elif type == 'json': #se for do tipo json rodar esse elif
        import json #importando a biblioteca json
        with open(file , 'w') as f: #abrindo o arquivo como write
            json.dump(obj, f) # fazendo o dump na variavel obj
    else:
        print('Serizalizacao invalida seu ignobio') # caraio hein, seu animal???

#deseralizing form a python object

def deserialize(file, type): #criando a função
    if type == 'pickle': # se o tipo for pickle
        import pickle # importando o dicionario
        with open(file, 'rb') as f: # abrindo o arquivo com read binary
            obj = pickle.load(f) # colocando o contudo na variavel 'obj'
        return obj # retornando obj
    elif type == 'json': # se o tipo for json
        import json # importa a biblioteca json
        with open(file, 'r') as f: # abrindo o arquivo com read
            obj = json.load(f) # fazendo o dump no variavel 'obj'
            return obj # retornando obj
    else:
        print('Serizalizacao invalida seu ignobio') # caraio hein, seu animal???

if __name__ == '__main__': 
    """
    Bloco de controle de execução. Esta é uma convenção padrão em Python. Significa: "Se este arquivo for executado diretamente (e não importado por outro módulo), execute o código abaixo." (A sua pergunta é respondida aqui!)
    """
 
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')} # dicionario utilziado para as funcoes

    #serialize using pickle
    serialize(d1, 'a.dat', 'pickle') # vai usar o dicionario 'd1', salvar no arquvio 'a.dat', e vai utilizar o metodo 'pickle' - SERIALIZANDO.

    #deserialiazing
    myDict = deserialize('a.dat', 'pickle') #usando a função deserialize utilziando o arquvio 'a.dat' criado com pickle
    print(f'pickle: {myDict}') # imprimindo

    print('#' * 20)#criar separador

    #serializing using json
