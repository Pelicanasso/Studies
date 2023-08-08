# functions basicaly is a task set under one name, ia form of organization 

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
    
text = convert_uppercase(upper_flag= True, texto = "Ryan")
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


