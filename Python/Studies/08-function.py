# functions basicaly is a task set under one name, is form of organization 

# Function EVAL receives a string input and convert, this input will be analised and converted
# for a python comand, he is one of the 70 functions natives from python

# Variable a and b that will be used in the equation
a = 2
b = 1
equation = input("Write the linear equation formula (a * x + b):")

#the x for the equation is in the FOR
for x in range(5):
    y = eval(equation)
    # the \n is for a line break
    print(f"\nResultado da equação para x = {x} é {y}")

print("===============================================================")

# Developing my own function, to make this i use the comand DEF

def print_a_message(day, hour):
    print(f"This is just a test for my first function, today is {day}, {hour}")

print_a_message("05/08/2023", "01:47 AM")

print("===============================================================")

# RETURN comand, with this the response of a function can be storaged in a variable

def testing_return(test):
    return(f"This here is just a text for return {test}")

function = testing_return(":)")
print(function)

print("============================================================")

# positional and mandatory parameters with default value add to parameters

def discount_calculate(value, discount = 0):
    final_price = value - (value * discount)
    return final_price

without_dicount = discount_calculate(100) #in this first he will use the default value for the discount
with_discount = discount_calculate(100, 0.25) #Here the discount value will be 0.25, or 25%

print(f"Total da compra: {without_dicount}")
print(f"Total da compra: {with_discount}")

print("===============================================================")

# positional and mandatory parameters doen't have interpretation error, so we can have logic error like this

def person_info(name, age, city):
    print("Info to be registered:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

person_info("Ryan", "21", "Presidente Prudente")
print("__________________")
person_info("Presidente Prudente", "Ryan", "21")

print("================================================================")

#Nominal parameters, the parameters will be identified by the name doens't matter the order

def convert_uppercase(text, upper_flag):
    if upper_flag:
        return text.upper()
    else:
        return text.lower()
    
text = convert_uppercase(upper_flag= True, text = "Ryan")
print(text)

# Exporing more the comand RETURN with another comand, SPLIT

def converting_month_to_extense(date): #creatimg function
    mes = ''' janeiro fevereiro março 
    abril maio junho julho agosto
    setembro outrubro novembro
    dezembro'''.split() #creating variable with the name of the months
    # SPLIT comand "break" the string for each blank space
    d, m, a = date.split("/") # now putting the character "/" to be the break parameter
    # also we use the multiple atribuition making the date format dd/mm/aaaa to be storaged in
    # each one of the variables, d = dd m = mm a = aaaa 
    extense_month = mes[int(m) - 1] # The first month will be in the 0 position
    # searching in the month list, picking the m variable and atributing to him one of month name
    return f"{d} de {extense_month} de {a}" #return the awsner now with the month for extense

# printing function inform the date to convert
print(converting_month_to_extense("05/08/2023"))

print("================================================================")

def convert_lowercase(text, lower_case = True):
    if lower_case:
        return text.lower()
    else:
        return text.upper()

text1 = convert_lowercase(lower_case = True, text = "LINGUAGEM DE PROGRAMAÇÃO")
text2 = convert_lowercase(text = "LINGUAGEM de programção")

print(f"\nTexto 1 = {text1}")
print(f"\nText 2 = {text2}")

print("================================================================")

#Creating a function with no defined number of parameters, doens't need to be called ARGS but is good practice, the * is obrigated
def print_parameters(*args):
    qtde_parameters = len(args) #LEN function returns the number of items in an object
    print(f"Number os parameters = {qtde_parameters}")

    for i, valor in enumerate(args): #ENUMERATE converts a data collection object into an enumerate object, the i will receive the position and value the value of the object
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1:")
print_parameters("São paulo", 10, 23.78, "João")

print(f"\nChamada 2:")
print_parameters(10, "São Paulo")

print("================================================================")

#function was defined a way he needs nominal parameters, using the **kwargs, doens't need to be called kwargs but is a good practice, the 2 * is obragated
def print_parameters1(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n") #TYPE returns the type of a information
    qtde_parameters =  len(kwargs) #LEN function returns the number of itens in a list
    print(f"Quantidade de parâmetros = {qtde_parameters}") 

    for chave, valor in kwargs.items(): 
        print(f"variável = {chave}, valor = {valor}")

print("\nChamada 1:")
print_parameters1(city = "Presidente Prudente", name = "Ryan", age = 21, height = 1.72)

print("\nChamada 2")
print_parameters1(discount = 10, value = 100)