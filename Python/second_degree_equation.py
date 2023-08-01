a = 2
b = 3
c = 7
#in a input the type of the variable will always be a string so we need to 
x = input("Insira o valor de x: ")

x = float(x) 

y = a * x ** 2 + b * x + c

print(f"o resultado do x é : {y}")