'''
    Set objects can be made by two ways:

    - Using a pair of keys with elements separeted by comma: set = {'a', 'b', 'c'}
    - Using the conturctor of type: set(iterable)

    we can't make a empty set, like this set{}, because this way we will crete a dictionary
'''

vogais = {'aeiou'} # without the contrutor

print(type(vogais), vogais)

vogais2 = set('aeiouaaaaaaaa') #constructor with string
print(type(vogais2), vogais2)

vogais3 = set(['a', 'e', 'i', 'o', 'u']) #constructor with a list inside
print(type(vogais3), vogais3)

vogais4 = set(('a', 'e', 'i', 'o', 'u')) #constructor with a tuple inside
print(type(vogais4), vogais4)

print(set("banana"))#na hora de imprimir ele irá contar os caracteres repetidos e ordenalos por ordem de aparição do maior número para o menor

print("\n======================================================================\n")

def create_report():
    componentes_verificados = set(["caixas de som", "cooler", 'dissipador de calor', 'cpu', 'hd', 'placa de som', 'placa de vídeo', 'ssd', 'estabilzador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória RAM', 'microfone', 'modem', 'placa-mãe', 'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])

    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)

    componentes_ok = componentes_verificados.difference(componentes_com_defeito)

    print(f"Número de componentes que foram verificados: {qtde_componentes_verificados}")
    print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito")
    print('\nOs compoenentes que podem ser vendidos são:')
    for item in componentes_ok:
        print("item:", item)

create_report()