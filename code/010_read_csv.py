import csv

with open('airtravel.csv', 'r') as f: #abriu o arquivo em read only
    reader = csv.reader(f) #colocou o conteudo do arquivo na variavel reader
    next(reader) # pulo a primeira linha
    year_1958 = dict() #cricou um dicionario vazio

    for row in reader:
        year_1958[row[0]] = row[1] #popula o dicionario

    # print(year_1958) #imprime o dicionário

    max_1958 = max(year_1958.values())#acha o valor maior

    # print(max_1958)#printa o valor maior

    for k, v in year_1958.items():
        if max_1958 == v:
            print(f'Busiest Month int 1958: {k}, Flights: {v.strip()}')