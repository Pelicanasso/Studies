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
print(min(frutas)) #The minimun is a word list is made by the alphabetical order
print(max(notas)) #MAX takes the maximum number in a list
print(frutas.count("maças"))
print(frutas + notas)
print(2 * frutas)

print("\n======================================================================\n")
