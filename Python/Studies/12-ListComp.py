linguagens = ['Python', 'Java', 'Kotlin', 'R', 'JavaScript', 'C', 'C++', 'Swift', 'Go']
#linguagens = '''Python Java Kotlin R C C++ Swift Go.split() this ia another way to achieve the same result above

print(f"\nAntes do ListComp = {linguagens}")

linguagens = [item.lower() for item in linguagens]#Lower puts very letter in lower case

print(f"Depois do ListComp lower = {linguagens}")

linguagens = [item.upper() for item in linguagens]#Upper puts every letter in upper case

print(f"Depois do ListComp Upper = {linguagens}")

print(f"\n==================================================================\n")

#second Way to make the same thing above

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()

print(f"\nDepois do ListComp = {linguagens}")

print("\n======================================================================\n")

linguagens_java = [item for item in linguagens if "java" in item]# "X is in S?"
linguagens_javav1 = [item for item in linguagens if "java" in item]

print(f"Depois do ListComp pegando as palavras da lista que contenha 'Java' = {linguagens_java}")
print(f"Depois do ListComp pegando somente a palavra 'java' = {linguagens_javav1}")

print("\n======================================================================\n")

#another way to make the same thing above
linguagens_javav2 = []
linguagens_javav3 = []

for item in linguagens:
    if 'java' in item:
        linguagens_javav2.append(item)

for item in linguagens:
    if item == 'java':
        linguagens_javav3.append(item)
        
print(linguagens_javav2)
print(linguagens_javav3)

print("\n======================================================================\n")

print('''
      Map() e filter() são duas funções do python que podemos aplicar nas listas
      
      map = utilizada para aplicar uma determinada função em cada item de um objeto iterável
      filter = mesmas características do map, mas ao invés de transformar os valores da lista, vamos filtra-los
      
      Exemplo 1\n '''
      )

new_list = map(lambda x: x.upper(), linguagens)
print(f"A nova lista é: {new_list}")

new_list = list(new_list)
print(f"Agora sim é a nova lista = {new_list}")

print("\nExemplo 2\n")

numbers = [0, 1, 2, 3, 4, 5]
square = list(map(lambda x: x*x, numbers))

print(f"Lista dos números antes de serem elevados: {numbers}")
print(f"Lista dos números elevados ao quadrado = {square}")

print("\n======================================================================\n")

numeros = list(range(0, 21))
print("\n Função Filter\n")

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))

print(f"Números pares do range(0,21): {numeros_pares}")
print(f"Números impares de range(0,21): {numeros_impares}")

print("\n======================================================================\n")




