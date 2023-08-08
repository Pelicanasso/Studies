"""
    This file is a challenge in the ebook A LINGUAGEM PYTHON from Vanessa Cadan Scheffer, Unit 1, section 1, foco no mercado de trabalha
    in this challenge i need to analyse a graph and based in the information in it make a code that will make prevision about the sales 
    from a store based in the month informed in the console
"""
month = input("Insert the desired month:")

month = int(month)

results= month * 200

print(F"The number of sales for the month {month} will be: {results}")