"""
    Relatinal Operators

    a < b : smaller than
    a <= : smaller or equal than
    a > b : higher than
    a >= b : higher or equal than
    a == b : equal
    a != b : different
    a is b : identic
    a is not b : not identic
"""
a = input("Insert the first number:")
b = input("Insert the second number:")

a = int(a)
b = int(b)

# Use of the if parameter, we need to set a condition for him
if a > b:
    print(f"The first number, {a}, is higher than the sencond number, {b}")
    print(f"The difference if for {a - b} units")

print("_____________________________________________________________________________")

# Use of the else parameter, the else is the opossite of the if
if a > b:
    print(f"The first number, {a}, is higher than the sencond number, {b}")
    print(f"Is higher for {a - b} units")
else:
    print(f"The second number, {b}, is higher than the first number, {a}")
    print(f"The difference is for {b - a} units")

print("_____________________________________________________________________________")

# Use of the elif parameter, he is a way to put more than only to option for a chained structure
# We can have a lot of elif

if a > b:
    print(f"The first number, {a}, is higher than the sencond number, {b}")
    print(f"Is higher for {a - b} units")
elif a == b:
    print(f"The two numbers are equal, {a} ")
else:
    print(f"The second number, {b}, is higher than the first number, {a}")
    print(f"The difference is for {b - a} units")