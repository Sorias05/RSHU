x=0
for i in range(1, 66):
    if(i%3==0 and i%5==0):
        x+=i
        print(f'Num: {i}')
print(f'Sum: {x}')