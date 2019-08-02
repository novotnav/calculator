operation = input("Choose the mathematical operation \n (a - addition, s - subtraction, m - multiplication, d - division): ")
nr_a = input("First number: ")
nr_b = input("Second number: ")

if operation is not "a" and operation is not "s" and operation is not "m" and operation is not "d":
    print("Please insert only letters a, s, m or d to choose the operation.")

try:
    val = int(nr_a)
    nr_a = int(nr_a)
except ValueError:
    print("Please insert only numbers.")
try:
    val = int(nr_b)
    nr_b = int(nr_b)
except ValueError:
    print("Please insert only numbers.")

if isinstance(nr_a, int) and isinstance(nr_b, int):
    add = nr_a + nr_b
    sub = nr_a - nr_b
    mul = nr_a * nr_b
    div = nr_a / nr_b

    if operation is "a":
        print("The result is: " + str(add))
    if operation is "s":
        print("The result is: " + str(sub))
    if operation is "m":
        print("The result is: " + str(mul))
    if operation is "d":
        print("The result is: " + str(div))


















