def result(a, b):
    return f'{a/100*(100-b)}'

a=float(input("Input 1 number: "))
b=-1
while(b < 0 or b > 100): b=float(input("Input 2 number (%): "))
print(result(a, b))