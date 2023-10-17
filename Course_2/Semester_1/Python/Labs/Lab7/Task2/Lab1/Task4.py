import math;

def result(a, b):
    return f'{math.ceil(b/a)}'

a=-1
b=-1
while(a < 0): a=float(input("Input 1 number: "))
while(b < 0): b=float(input("Input 2 number: "))
print(result(a, b))