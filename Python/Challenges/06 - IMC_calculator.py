'''
    This is a challenge to create a calculator of IMC
    firts i need to discovered what are the formula for this calculation
    and the formula is:
        IMC = weight/height²
    then create based in the intervals of the results a series 

    information font: https://www.tuasaude.com/imc/
'''

print('''
    Calculadora de IMC\n

    O índice de massa corporal(IMC) é uma medida internacional 
    usada para calcular se uma pessoa está no peso ideal.
    Para usar essa calculadora basta informar 
    seu peso e sua altura, o calculo será feito
    e o resultado entregue com a classificação.
    Veja abaixo a tabela de classificações\n
      
        IMC	Classificação\n
    < 18,5	         Magreza
    18,5 a 24,9	         Peso normal
    25 a 29,9	         Sobrepeso
    30 a 34,9	         Obesidade grau I
    35 a 39,9	         Obesidade grau II
    > 40	         Obesidade grau III
    ''')

peso = float(input("Informe seu peso em quilos: "))
alt = float(input("Informe sua altura em metros: "))
imc = peso / pow(alt, 2)

if imc < 18.5:
    print("Abaixo do peso")
    print(f"Seu IMC: {imc}")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
    print(f"Seu IMC: {imc}")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
    print(f"Seu IMC: {imc}")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau I")
    print(f"Seu IMC: {imc}")
elif imc >=35 and imc <=39.9:
    print("Obesidade grau II")
    print(f"Seu IMC: {imc}")
else:
    print("Obesidade Grau III")
    print(f"Seu IMC: {imc}")

