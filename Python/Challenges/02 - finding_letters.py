# This is a second level from the fingding letter a and e, now i have to find all vowels in a text and give the total of vowel

text = input("This code will extract every vowel in a text and give the total of them, insert a text:")
x = 0

for i, c in enumerate(text):
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        x = x + 1
        print(f"Posição = {i}, letra = {c}")
    else:
        continue;

print(f"Total de vogais: {x}")