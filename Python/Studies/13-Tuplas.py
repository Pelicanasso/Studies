'''
Tuplas are data structures from the group of objects sequence type, the big difference from the list
are in the fact they are not mutable, you can't change them

to build a Tupla have three ways:

- DOuble parentheses to denot a empty tupla : tupla1 = ()
- Double parentheses with elements separeted by comma: tupla1 = ('a', 'b', 'c')
- Using the contructor of type: tuple()
'''

vogais = ('a', 'e', 'i', 'o', 'u')

print("Usando as Tuplas\n")
print(f"Tipo de objeto vogais = {type(vogais)}")

for position, value in enumerate(vogais):
    print(f"Posição = {position}, valor = {value}")


print(tuple(enumerate(vogais)))
print(list(enumerate(vogais)))
