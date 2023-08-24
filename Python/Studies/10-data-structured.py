'''
    data structured ia a finite sequence index by non negative numbers
    the first elements of a sequence ocups the position 0, the last n-1 
'''

text = "learningn Python while my anxiety and thougts are decaying my mental health"

print(f"\nNumber of characters: {len(text)}")
print(f"Python in text: {'Python' in text}")
print(f"Number of 'y' in the text: {text.count('y')}")
print(f"Cinco primeiras posições da string : {text[0:6]}")

print("\n===========================================================================\n")

print(text.upper()) #UPPER command sets all worls of the text to upper case
print(text.replace("i", 'XX')) #REPLACE command as the name says will replace a character we inform to other, first 

print("\n===========================================================================\n")

#SPLIT function cut the text and transform based on a parameter(if not informed he breaks in every blank space) him in a list

print(f"Texto inteiro antes de ser feito o Split = {text}")
print(f'Tamanho do texto = {len(text)}')

words = text.split() #Applying the SPLIT and associating him to a variable
print(f"Palavras = {words}") #Printing this new variable
print(f"Number of words = {len(words)}") #this result will be "12" because he count for word

print("==================================================================================")

text2 = '''Operators String
Pyhton offers operators to process text(strings).
Like the numbers, strings can be compared using comparision operators:
==, !=, <, >, etc
The operator ==, will return 'True' if the strings has the same value
'''

print(f"Texto antes de passar por qualquer alteração = {text2}")
print(f"Tamanho do texto = {len(text2)}") # counting the number of characters
text2 = text2.lower() #LOWER function will put every word in lower case
text2 = text2.replace(",", ""). replace (".", "").replace("(", "").replace("\n", "") # making a chain of replaces in my text, in this case i'm replacing a lot of itens for nothing so i'm deleting the selected itens
print(f"Text after the replace = {text2}") 
word_list = text2.split() #breaking the string for every blank space and creating a list of itens in a new variabel
print(f"Tamanho da lista de palavras = {len(word_list)}") 

total = word_list.count("string") + word_list.count("strings") #COUNT function returns a int value so we can make mathematical function with him like this one

print(f"Quantidade de vezes que 'string' ou 'strings' apareceu = {total}")

print(f"===============================================================================================")
