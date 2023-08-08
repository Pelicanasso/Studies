"""
    and = takes two elements(a and b), the result will be true only when the two elements are true
    or = when one of the elements are true the results will be true, dons't need the two to be true
    not = invert the element, true = false and false = true 

    like mathematic the boolean structure follows rules order for reoslution
    NOT first, AND second and OR is the last
"""

num_miss = int(input("Total of miss in school: "))
final_note = float(input("Final note of the student: "))

A = 15
B = 9
C = 9

# AND structure

if num_miss <= 5 and final_note >= 7:
    print("Approved student")
else:
    print("Reproved student")

print("__________________________________________________________________")

# OR structure

if num_miss <= 5 or final_note >= 7:
    print("Approved student")
else:
    print("Reproved student")

print("__________________________________________________________________")

#Boolean order resolution exemple

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C)

print("__________________________________________________________________")

