n = int(input("Enter number: "))
result = 0
res = 2
i = 0
while result != res:
    i += 1
    res = 2
    for j in range(i):
        if res == n:
            result = res
        elif res * 2 > n:
            result = res
        else:
            res *= 2

print(result)
    
    