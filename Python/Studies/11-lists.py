vogais = ['a', 'e', 'i', 'o', 'u'] #creating a list

for vogal in vogais:
    print(f"Posição = {vogais.index(vogal)}, valor = {vogal}") #INDEX returns the position of a value in a sequence

print("\n=================================================\n")

vogais1 = [] #creating a blank list

print(f"Type of object vogais1 = {type(vogais)}")
vogais1.append("a") #APPEND add a new value to the end of the list
vogais1.append("e")
vogais1.append("i")
vogais1.append("o")
vogais1.append("u")

for p, x in enumerate(vogais1): #ENUMERATE function returns the value and position of a object in the list
    print(f"Posição = {p}, valor = {x}")

print("\n==================================================================\n")

frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas)
print("abacate" in frutas)
print("abacate" not in frutas)
print(min(frutas)) #The minimun in a word list is made by the alphabetical order
print(max(notas)) #MAX takes the maximum number in a list
print(frutas.count("maça"))
print(frutas + notas)
print(2 * frutas)

print("\n======================================================================\n")

list = ["Java", 3.10, "Python", ["a", "b", 20], 25, "Sei lá"]

print("\nExemplo de Slices\n")

print(f"Lista[1] = {list[1]}")#taking the second element from a list, the list initiate from 0
print(f"List [1:2] = {list[0:2]}")
print(f"Lista[:2] = {list[:2]}")
print(f"Lista[3:5] = {list[3:5]}")
print(f"List[3:6] = {list[3:6]}")
print(f"Lista[3:] = {list[3:]}")
print(f"Lista[-2] = {list[-2]}") #the negative prompt go to the end of the list and makes the reverse counting
print(f"Lista[-1] = {list[-1]}")
print("Lista[4][1] =", list[3][1]) #accessing a internal value inside the list that are inside another list

print("\n======================================================================\n")