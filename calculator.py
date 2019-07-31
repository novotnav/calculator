operation = input("Zadejte požadovanou matematickou operaci (1 - sčítání, 2 - odčítání, 3 - násobení, 4 - dělení): ")
nr_a = input("První číslo: ")
br_b = input("Druhé číslo: ")

if operation == 1:
    add = nr_a + nr_b
print("Výsledek: " + add)

if operation == 2:
    sub = nr_a - nr_b
print("Výsledek: " + sub)

if operation == 3:
    mul = nr_a * nr_b
print("Výsledek: " + mul)

if operation == 4:
    div = nr_a / nr_b
print("Výsledek: " + div)
