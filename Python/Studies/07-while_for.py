"""
    the WHILE and FOR comand are used to create loopings
"""
# WHILE is more used in servers to repeat some comands, like for 20 hours in a row
num = 1
name = 'Ryan'
classroom = "Python class"

while num != 0:
    
    num=int(input("Digite um número:"))
    if num % 2 == 0:
        print("Esse número é par!")
    else:
        print("Esse número é ímpar!")

print("End of the execution!")
print('_______________________________________________________________')

# FOR, creating the variable c and saying he belong to name, name is a string that is basicaly a array

for c in name:
    print(c)

print("_______________________________________________________________")

# FOR with ENUMERATE, this function returns the position of each item

for i, c in enumerate(name):
    print(f'Posição = {i}, valor = {c}')
print("___________________________________________________________")

"""
     FOR with RANGE he is used to create a numbered sequence
     we have 3 methods to do this
     1 = informing the number of repetions
     2 = with two arguments, one that represents the start and other the limit
     3 = with three arguments, one for the start, one ofr the limit and the last for the increment
"""
print("Method 1")
for i in range(10):
    print(i)

print("Method 2")
for i in range(5, 10):
    print(i) 

print("Method 3")
for i in range (4, 24, 4):
    print(i)

print("__________________________________________________________________")

"""
    BREAK and CONTINUE comands
    BREAK: stops the execution of a structure of repetition
    CONTINUE: "jump" some some execution based in the condition
"""
for i in classroom:
    if i == "a":
        break
    else:
        print(i)

print("===========")

for i in classroom:
    if i == "a":
        continue
    else:
        print(i)

