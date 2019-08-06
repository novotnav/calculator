print("This calculator factorizes two given numbers to prime numbers.")
x = input("Insert the first number you want to factorize: ")
y = input("Insert the second number you want to factorize: ")

point_x = int(x)
div_x = int(2)
arr_x = []
while div_x <= point_x:
    rem_x = point_x % div_x
    if rem_x is 0:
        arr_x.append(div_x)
        point_x = int(point_x / div_x)
    else:
        div_x = int(div_x + 1)
if div_x > point_x:
    print(arr_x)

point_y = int(y)
div_y = int(2)
arr_y = []
while div_y <= point_y:
    rem_y = point_y % div_y
    if rem_y is 0:
        arr_y.append(div_y)
        point_y = int(point_y / div_y)
    else:
        div_y = int(div_y + 1)
if div_y > point_y:
    print(arr_y)
