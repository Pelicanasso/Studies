print("====================================================\n")

print(''' Calculadora \n
      será solicitado dois números
      para a operação basta escrevê-la\n''')

print("=====================================================\n")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
oper = input("Digite a operação desejada: ")

def calculator(num1, num2, operator):
    operator = operator.lower()
    if operator == "mais" or operator == "soma":
        return num1 + num2
    elif operator == "menos" or operator == "subtração":
        return num1 - num2
    elif operator == "vezes" or operator == "multiplicação":
        return num1 * num2
    elif operator == "divisão":
        return num1 / num2
    else:
        print("Operador inválido!")
        return 0
    
resultado = calculator(num1, num2, oper)
print(f"\nResultado da conta: {resultado}")