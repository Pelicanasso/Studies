# basicaly i describe the objective of the challenge in the variable

text = input("This code will extract the position of the vowels a and e from a text, inform the text:")

for i,c in enumerate(text):
    if c == "a" or c == "e":
        print(f"Posição = {i}, letra = {c}")
    else:
        continue;