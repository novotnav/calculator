operation = input("Choose the mathematical operation \n (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division): ")
nr_a = input("First number: ")
nr_b = input("Second number: ")

try:
    val = int(operation)
    operation = int(operation)
    if operation > 4:
        print("Please use only numbers 1 - 4 to choose the operation")
except ValueError:
    print("Please use only numbers 1 - 4 to choose the operation")

try:
    val = int(nr_a)
    nr_a = int(nr_a)
except ValueError:
    print("Please insert only numbers")
try:
    val = int(nr_b)
    nr_b = int(nr_b)
except ValueError:
    print("Please insert only numbers")

if isinstance(nr_a, int) and isinstance(nr_b, int):
    add = nr_a + nr_b
    sub = nr_a - nr_b
    mul = nr_a * nr_b
    div = nr_a / nr_b

    if operation == 1:
        print("The result is: " + str(add))
    if operation == 2:
        print("The result is: " + str(sub))
    if operation == 3:
        print("The result is: " + str(mul))
    if operation == 4:
        print("The result is: " + str(div))


















