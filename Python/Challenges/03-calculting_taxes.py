"""
    In this challenge i need to write a code for the store a worked before in the first challenge
    now he want a code to calculate the taxes of his employes
"""

renda = float(input("report your salary for tax calculation: "))
"""
if renda <= 1903.98:
    print("You don't have to pay taxes")
elif renda > 1903.99 and renda <= 2826.65:
    print("You have to pay R$142,80 of taxes")
elif renda > 2826.66 and renda <= 3751.05:
    print("You have to pay R$354,80 of taxes")
elif renda > 3751.06 and renda <= 4664.68:
    print("You have to pay R$636,13 of taxes")
else:
    print("You have to pay R$869,36 of taxes")

this was my first try but after thinking again i can reduce this code, i don't need the
AND the way the codes works i can remove him and will do the same thing
"""

if renda <= 1903.98:
    print("You don't have to pay taxes")
    print(f"Salary: {renda}")
elif renda <= 2826.65:
    print("You have to pay R$142,80 of taxes")
    print(f"Salary with disount: {renda - 142.80}")
elif renda <= 3751.05:
    print("You have to pay R$354,80 of taxes")
    print(f"Salary with disount: {renda - 354.80}")
elif renda <= 4664.68:
    print("You have to pay R$636,13 of taxes")
    print(f"Salary with disount: {renda - 636.13}")
else:
    print("You have to pay R$869,36 of taxes")
    print(f"Salary with disount: {renda - 869.36}")
          