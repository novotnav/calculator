operation = input("Choose the mathematical operation \n (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division): ")
nr_a = input("First number: ")
nr_b = input("Second number: ")



nr_a = int(nr_a)
nr_b = int(nr_b)
operation = int(operation)

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
