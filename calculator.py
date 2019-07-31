operation = input("Zadejte požadovanou matematickou operaci (1 - sčítání, 2 - odčítání, 3 - násobení, 4 - dělení): ")
nr_a = input("První číslo: ")
nr_b = input("Druhé číslo: ")

nr_a = int(nr_a)
nr_b = int(nr_b)
operation = int(operation)

add = nr_a + nr_b
sub = nr_a - nr_b
mul = nr_a * nr_b
div = nr_a / nr_b

if operation == 1:
    print("Výsledek: " + str(add))

if operation == 2:
    print("Výsledek: " + str(sub))

if operation == 3:
    print("Výsledek: " + str(mul))

if operation == 4:
    print("Výsledek: " + str(div))
