def ToCurr(x):
    c500=0; c100=0; c10=0; c5=0; c1=0
    while (x >= 500): c500=c500+1; x=x-500
    while (x >= 100): c100=c100+1; x=x-100
    while (x >= 10): c10=c10+1; x=x-10
    while (x >= 5): c5=c5+1; x=x-5
    while (x >= 1): c1=c1+1; x=x-1
    return (f'{c500} (500), {c100} (100), {c10} (10), {c5} (5), {c1} (1)')
a=-1
b=-1
c=-1
while(a < 0): a=int(input("Input 1 number: "))
while(b < 0): b=int(input("Input 2 number: "))
while(c < 0): c=int(input("Input 3 number: "))
print(ToCurr(a))
print(ToCurr(b))
print(ToCurr(c))