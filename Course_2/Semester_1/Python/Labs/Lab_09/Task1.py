op_set = {'+', '-', '/', '*', 'mod', 'pow', 'div'}
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

flag = False
while(flag == False):
    op = input("Enter operator (+, -, /, *, mod, pow, div): ")
    for el in op_set:
        if(el == op):
            flag = True

if(op == '+'):
    print(f'{n1} + {n2} = {n1 + n2}')
if(op == '-'):
    print(f'{n1} - {n2} = {n1 - n2}')
if(op == '/'):
    try:
        print(f'{n1} / {n2} = {n1 / n2}')
    except ZeroDivisionError:
        print("Division by zero!")
if(op == '*'):
    print(f'{n1} * {n2} = {n1 * n2}')
if(op == 'mod'):
    try:
        print(f'{n1} % {n2} = {n1 % n2}')
    except ZeroDivisionError:
        print("Division by zero!")
if(op == 'pow'):
    print(f'{n1} ^ {n2} = {n1 ** n2}')
if(op == 'div'):
    try:
        print(f'{n1} // {n2} = {n1 // n2}')
    except ZeroDivisionError:
        print("Division by zero!")

