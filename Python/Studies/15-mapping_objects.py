'''
    estruturas de dados que contém um mapeamente entre uma chave e um valor são considerados objetos do tipo mapping
    the object that have this propriety is the dict(dictionary)

    we can build the dictionary iun three ways:
     -Using a pais of keys to create a empty dict: dict1 = {}
     -Using a pair of elements in the form, key: value separeted  by comma: dict1 = {'one':1, 'two':2, 'three':3}
     -Using the constructor of type: dict()
'''

#exemple 1 - creating a empty dictionary, with posterior atribuittion of key and value

dici_1 = {}
dici_1['Nome'] = 'João'
dici_1['Idade'] = 30
dici_1['Cidade'] = "P. Prudente"

#exemple 2 - Creating a dictionary using the par of elements in the form, key:value
dici_2 = {'Nome':'João', 'Idade':30, "Cidade":'P. Prudente'}

#exempe 3 - Creating a dictionary with a tuple list, the tuples represents a pair of key:value
dici_3 = dict([('Nome', 'João'), ('Idade', 30), ("Cidade", "P. Prudente")])

#exemple 4 - creating a dictionary with the build-in fucntion zip() and two list, one with keys, other with the values
dici_4 = dict(zip(['Nome', 'Idade', 'Cidade'], ['João', 30, 'P. Prudente']))


print(dici_1)
print(dici_2)
print(dici_3)
print(dici_4, "\n")

print(dici_1 == dici_2 == dici_3 == dici_4)

print("\n======================================================================\n")

cadastro = {
    'Nome': ['João', 'Ryan', 'Erick', 'Salomão', 'Barbára'],
    'Cidade':['Pirapó', 'P. Prudente', 'Paraná', 'Nandes', 'P. Prudente'],
    'Idade': [27, 21, 20, 28, 21]
}

print(f"Len(casdastro): {len(cadastro)}")

print(f"\nCadastro.keys() = {cadastro.keys()}")
print(f"\nCadastro.values() = {cadastro.values()}")
print(f"\nCadastro.items() = {cadastro.items()}")

print(f"\ncadastro['nome'] = {cadastro['Nome']}")
print(f"cadastro['idade'][2] = {cadastro['Idade'][2]}")
print(f"cadastro['cidade'][2:] = {cadastro['Cidade'][2:]}")

'''
cadastro.keys(): retorna uma lista com todas as chaves no dicionário.
cadastro.values(): retorna uma lista com os valores. Como os valores também são listas, temos uma lista de listas.
cadastro.items(): retorna uma lista de tuplas, cada uma das quais é composta pela chave e pelo valor.
cadastro['nome']: acessa o valor atribuído à chave 'nome'; nesse caso, uma lista de nomes.
cadastro['nome'][2]: acessa o valor na posição 2 da lista atribuída à chave 'nome'.
cadastro['idade'][2:]: acessa os valores da posição 2 até o final da lista atribuída à chave 'nome'.
'''
print(f"\nQuantidade de nomes: {len(cadastro['Nome'])}")
print(f"Quantidade de cidade: {len(cadastro['Cidade'])}")
print(f"Quantidade de Idades: {len(cadastro['Idade'])}")

total = sum([len(cadastro[chave]) for chave in cadastro]) #sum() para somar e obter a quantidade total de itens

print(f"\nQuantidade total de elementos no dicionário = {total}")
