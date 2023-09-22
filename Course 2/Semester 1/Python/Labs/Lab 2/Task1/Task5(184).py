n = int(input("Enter length of bar of chocolate (the amount of pieces): "))
m = int(input("Enter width of bar of chocolate (the amount of pieces): "))
k = int(input("Enter number of pieces: "))
a = ''
for i in range(n):
    if(i * m < k):
        a = "No"
    elif(i * m == k):
        a = "Yes"
        break
if(a != "Yes"):
    for i in range(m):
        if(i * n < k):
            a = "No"
        elif(i * n == k):
            a = "Yes"
            break
print(a)