value = float(input("Digite o valor o do produto: "))
qtde = int(input("Digite o número de produtos: "))
currency = input("Qual a moeda: ")

def total_sells(value, qtde, currency = "real"):
    currency = currency.lower()
    if currency == "real":
        total = qtde * value
        print(f"Total da compra: {total}")
    elif currency == "euro":
        totalR = qtde * (value * 5.70)
        totalE = qtde * value
        print(f"Total da compra em Reais = {totalR}")
        print(f"Total da compra em Euro = {totalE}")
    elif currency == "dolar":
        totalR = qtde * (value * 5)
        totalD = qtde * value
        print(f"Total da compra em Reais: {totalR}")
        print(f"Total da compra em Dólar: {totalD}")
    else:
        print("Tipo de moeda inválida")

print("Primeira versão apenas com os itens obrigratórios:\n")
total_sells(value, qtde, currency)

print("==========================================\n")

print("Segunda versão com descontos e acréscimos \n")

def total_sellsv2(value, qtd, currency, discount = None, increase = None):
    brute_value = qtd * value

    if discount:
        liquid_value = brute_value -(brute_value *(discount/100))
    elif increase:
        liquid_value = brute_value +(brute_value*(increase/100))
    else:
        liquid_value = brute_value

    if currency == "real":
        return liquid_value
    elif currency == "dolar":
        return liquid_value * 5
    elif currency == "euro":
        return liquid_value * 5.7
    else:
        print("Moeda inválida")
        return 0
    
totalv2 = total_sellsv2(value, qtde, currency, discount = 25)
print (f"Total da compra: {totalv2}")

print("==========================================\n")

print("Terceira solução possível \n")

def total_sellsv3(value, qtde, currency = "real", **kwargs):
    brute_value = value * qtde

    if "desconto" in kwargs:
        desconto = kwargs["desconto"]
        liquid_value = brute_value -(brute_value *(desconto/100))
    elif "acrescimo" in kwargs:
        acrescimo = kwargs["acrescimo"]
        liquid_value =  brute_value +(brute_value *(acrescimo/100))
    else:
        liquid_value = brute_value

    if currency == "real":
        return liquid_value
    elif currency == "dolar":
        return liquid_value * 5
    elif currency == "euro":
        return liquid_value * 5.7
    else:
        print("Moeda inválida")
        return 0
                                      
    
totalv3 = total_sellsv3(value, qtde, currency, desconto = 10)
print(f"Total da compra: {totalv3}")